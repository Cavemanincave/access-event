# Руководство администратора AccessEvent

## 1. Системные требования
- Python 3.11+
- PostgreSQL 15+
- Docker & Docker Desktop

## 2. Развёртывание и запуск
С использованием Docker (рекомендуется):
```bash
docker compose up -d
```
Локально:
1. `pip install -r requirements.txt`
2. Настроить конфигурационный файл `.env`.
3. `python app.py`

## 3. Матрица ролей и прав доступа
- `guest`: просмотр списка опубликованных мероприятий.
- `user`: регистрация на события, текстовый чат, просмотр уведомлений.
- `organizer`: создание, изменение и удаление собственных мероприятий.
- `admin`: полное управление пользователями, модерация чатов.

## 4. Резервное копирование БД
Создание бэкапа:
```bash
pg_dump -U postgres accessevent > backup.sql
```
Восстановление:
```bash
psql -U postgres accessevent < backup.sql
```
