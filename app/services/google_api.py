from datetime import datetime
from typing import List

from aiogoogle import Aiogoogle

from app.core.config import settings

FORMAT = "%Y/%m/%d %H:%M:%S"


async def spreadsheets_create(wrapper_service: Aiogoogle) -> str:
    """
    Создание нового Google Spreadsheet и возвращение его идентификатора.
    """
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_service.discover(
        api_name='sheets',
        api_version='v4'
    )
    spreadsheet_body = {
        'properties': {
            'title': f'Отчет от {now_date_time}',
            'locale': 'ru_RU'
        },
        'sheets': [
            {'properties': {
                'sheetType': 'GRID',
                'sheetId': 0,
                'title': 'Топ проектов по скорости закрытия',
                'gridProperties': {
                    'rowCount': 100,
                    'columnCount': 11
                }
            }}
        ]
    }
    spreadsheet_body['properties']['title'] += datetime.now().strftime(FORMAT)
    response = await wrapper_service.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    return response['spreadsheetId']


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
) -> None:
    """
    Установка прав на доступ к Spreadsheet для конкретного пользователя.
    """
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.email}
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields="id"
        ))


async def spreadsheets_update_value(
        spreadsheet_id: str,
        projects: List,
        wrapper_service: Aiogoogle
) -> None:
    """
    Обновление значения ячеек Google Spreadsheet.
    """
    service = await wrapper_service.discover(
        api_name='sheets',
        api_version='v4'
    )
    table_values = [[
        'Название проекта',
        'Время сбора',
        'Описание'
    ],
        *[list(map(
            str,
            [project['name'],
             project['interval'],
             project['description']])) for project in projects]
    ]
    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    await wrapper_service.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range='A1:C30',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
