from typing import Optional, List, Dict

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDCharityProject(CRUDBase):
    """
    CRUDCharityProject - класс для взаимодействия с моделью CharityProject в базе данных.
    """

    @staticmethod
    async def get_charity_id_by_name(
            charity_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        """
        Данная функция предназначена для получения id
        благотворительного проекта по его названию.
        """
        charity_id = await session.execute(select(CharityProject.id).where(
            CharityProject.name == charity_name
        ))
        charity_id = charity_id.scalars().first()
        return charity_id

    @staticmethod
    async def get_projects_by_completion_rate(session: AsyncSession) -> List[Dict[str, str]]:
        """
        Данная функция получает список завершенных благотворительных проектов и возвращает отчет о времени,
        затраченном на каждый из проектов.
        """
        projects = await session.execute(select([CharityProject]).where(CharityProject.close_date.isnot(None)))
        projects = projects.scalars().all()
        project_list = [{
            'name': project.name,
            'interval': project.close_date - project.create_date,
            'description': project.description
        } for project in projects]
        project_list = sorted(project_list, key=lambda x: x['interval'])
        return project_list


charity_crud = CRUDCharityProject(CharityProject)
