# Lunch Decider API — INFORCE Python Task

**Внутрішній сервіс для голосування за обід.**  
Ресторани завантажують меню щодня через API.  
Співробітники голосують за улюблене меню через мобільний додаток.

---

## Функціонал

- **JWT авторизація**
- **Підтримка `X-Build-Version`** з хедерів (обидві версії додатку)
- **Один голос на співробітника на день**
- **Меню на кожен день**
- **Результати голосування в реальному часі**

---

## Технології

| Технологія | Призначення |
|----------|-----------|
| Django + DRF | Backend, REST API |
| JWT | Авторизація |
| PostgreSQL | База даних |
| Docker + docker-compose | Контейнеризація |
| PyTest | 7+ різноманітних тестів |
| **flake8** | Лінтинг коду (бонус) |

---

## Архітектура (SOLID)

Проєкт побудовано за принципами **SOLID** — логіка рознесена по модулях:


backend/
├── employees/
│   ├── services.py     → створення користувача, оновлення build_version
│   └── tests/          → юніт-тести
├── restaurants/
│   └── tests/
├── menus/
│   ├── services.py     → створення голосу, підрахунок результатів
│   ├── validators.py   → перевірка дати, унікальності голосу
│   └── tests/          → 7+ тестів (успіх, помилки, edge cases)
└── lunch_decider/      → settings, urls


---

## Запуск системи

```bash
# 1. Клонувати проєкт
git clone https://github.com/Yurashpak887/lunch-decider
cd lunch_decider

# 2. Запустити Docker
docker compose up --build

API: http://localhost:8000
Адмінка: http://localhost:8000/admin

```

## Створення суперюзера
```bash
docker compose exec web python manage.py createsuperuser
```
## API Ендпоінти

| Метод | URL | Опис | Хедери |
|-------|-----|------|--------|
| `POST` | `/api/auth/login/` | Логін (JWT) | `X-Build-Version` |
| `POST` | `/api/employees/register/` | Реєстрація | `X-Build-Version` |
| `POST` | `/api/restaurants/` | Створити ресторан | `Authorization: Bearer <token>` |
| `POST` | `/api/menus/create/` | Додати меню на сьогодні | `Authorization: Bearer <token>` |
| `GET` | `/api/menus/today/` | Меню на сьогодні | `Authorization: Bearer <token>` |
| `POST` | `/api/menus/vote/` | Проголосувати | `Authorization: Bearer <token>` |
| `GET` | `/api/menus/results/` | Результати | `Authorization: Bearer <token>` |

> **Важливо:** `employee` береться з JWT, **не передається в body**.
> 

## Приклад запиту (Postman)
```bash

POST http://localhost:8000/api/menus/vote/
Authorization: Bearer <jwt_token>
Content-Type: application/json

{
  "menu": 1
}
```
## Тести
Покриття: створення голосу, валідація дати, унікальність, результати
Використовується pytest-django + fixtures
