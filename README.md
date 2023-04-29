# QRKot приложение

## Обзор

**QRkot** - QRkot является проектом, основанным на FastAPI, предназначенным для сбора средств для благотворительных проектов. Сервис обеспечивает регистрацию пользователей, добавление благотворительных проектов и пожертвований, которые распределяются по открытым проектам. Также имеется функционал для формирования отчетов в Google Sheets.

## Основные технологии и библиотеки:
- [Python](https://www.python.org/); 3.10
- [FastAPI](https://fastapi.tiangolo.com/);
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/);
- [Pydantic](https://pypi.org/project/pydantic/);

## Установка
1. Склонируйте репозиторий:
```
https://github.com/Lexxar91/QRkot_spreadsheets
```
2. Активируйте виртуальное окружение и установите зависимости. Предпочтительная версия Python - 3.10:
```
python -m venv venv
source venv/Scripts/activate
python -m pip install -U pip
pip install -r requirements.txt
```
3. Создайте в корневой директории файл .env со следующим содержанием:
```
APP_TITLE=QRkot
APP_DESCRIPTION=Приложение для Благотворительного фонда поддержки котиков QRKot
DATABASE_URL='sqlite+aiosqlite:///./fastapi.db'
SECRET=<secret>
FIRST_SUPERUSER_EMAIL=<email superuser>
FIRST_SUPERUSER_PASSWORD=<password superuser>
TYPE=service_account
PROJECT_ID=atomic-climate-<идентификатор>
PRIVATE_KEY_ID=<id приватного ключа>
PRIVATE_KEY="-----BEGIN PRIVATE KEY-----<приватный ключ>-----END PRIVATE KEY-----\n"
CLIENT_EMAIL=<email сервисного аккаунта>
CLIENT_ID=<id сервисного аккаунта>
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=<ссылка>
EMAIL=<email пользователя>

```
4. Если необходимо, примените миграции, чтобы создать базу данных SQLite:
```
alembic init --template async alembic
alembic revision --autogenerate -m "name migration"
alembic upgrade head
```
5. Проект готов к запуску.

Для запуска локального сервера используйте команду:
```
uvicorn app.main:app --reload
```
Сервис будет запущен и доступен по следующим адресам:
- http://127.0.0.1:8000 - API
- http://127.0.0.1:8000/docs - автоматически сгенерированная документация Swagger

### Автор
Муратов Дмитрий
https://github.com/Lexxar91