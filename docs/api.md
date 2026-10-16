# Описание API AccessEvent

| Метод | URL | Доступ | Вход (JSON) | Ответы |
|---|---|---|---|---|
| POST | /api/register | Все | username, email, password, role | 201 user_id; 400 ошибки валидации |
| POST | /api/login | Все | email, password | 200 token, role; 401 неверные данные |
| GET | /api/events | Все | — | 200 JSON-список всех мероприятий |
| POST | /api/events | Organizer | title, event_date, is_inclusive | 201 event_id; 401 без токена |
| POST | /api/registrations | User | event_id, accessibility_request | 201 id; 400 повторная запись |

## Примеры JSON-запросов

### POST /api/register
```json
{
  "username": "anna",
  "email": "anna@mail.ru",
  "password": "Passw0rd!",
  "role": "user"
}
```
### Ответ (201 Created)
```json
{
  "message": "Пользователь создан",
  "user_id": 1
}
```