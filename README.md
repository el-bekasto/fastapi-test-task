# fastapi-test-task

Упрощенное API электронного журнала оценок.

## Эндпоинты

### Ученики
 - POST   /student              - Создание ученика в базе данных
 - GET    /student/{student_id} - Получение ученика по айди из базы
 - PATCH  /student/{student_id} - Изменение ученика в базе по айди
 - DELETE /student/{student_id} - Удаление ученика из базы по айди

### Оценки
 - POST   /grade            - Создание оценки в базе данных
 - GET    /grade/{grade_id} - Получение оценки по айди из базы
 - PATCH  /grade/{grade_id} - Изменение оценки в базе по айди
 - DELETE /grade/{grade_id} - Удаление оценки из базы по айди

## Использованный стек
 - **FastAPI**
 - **SQLAlchemy**
 - **Alembic** (для миграций)

## Дополнительные фичи
 - Добавил рейтинг ученика, который возвращает его среднюю оценку
 - Добавил миграции для удобного изменения и инициализации БД

## Как запустить?
 1. Установить последнюю версию Python, создать папку проекта `fastapi_test` и перейти туда
 2. Клонировать туда проект командой `git clone https://github.com/el-bekasto/fastapi-test-task.git` и перейти в папку `fastapi-test-task`
 3. Создать виртуальное окружение командой `python -m venv venv`
 4. Активировать окружение (для Windows `.\venv\Scripts\activate`, для Linux source `.\venv\bin\activate`)
 5. Установить нужные пакеты командой `pip install -r requirements.txt`
 6. Выполнить миграции командой `alembic upgrade head`
 7. Запустить сервер командой `uvicorn main:app --host localhost --port 80` (вместо 80 можно использовать другой порт)
 8. Перейти к документации API по адресу http://localhost:80/docs (вместо 80 вставьте свой порт если он другой) и наслаждаться!