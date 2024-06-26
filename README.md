# AbsolutPOS

### Технологии:
+ Python
+ Django
+ PostgreSQL
___
### Инструкция по запуску приложения:

+ Клонируем репозиторий. (Проект сделан одним коммитом, так как проект небольшой).
+ Переходим в директорию проекта.
+ Создаем, затем активируем виртуальное окружение в терминале.

```
venv\Scripts\Activate
```
+ Установка зависимостей.
```pip install -r requirements.txt```
Database и Secret_key скрыты в .env файле. Пример, как он выглядит:
```angular2html

SECRET_KEY=django-insecure-c@_@kw^...


DB_NAME=blank
DB_USER=blank
DB_PASSWORD=blank
DB_HOST=localhost
DB_PORT=5432
```

+ Замените secret_key без кавычек, а также настройки database **Engine**, **Name**, **User**, **Password** на свои реальные.
+ Выполните миграции в терминале:
```angular2html
python manage.py makemigrations
python manage.py migrate
```
+ Создайте суперпользователя:
```
python manage.py createsuperuser
```

+ Запуск проекта:
```
python manage.py runserver
```
___
## Пользовательская документация

### Введение:
Код представляет часть проекта будущего проекта, разработанного создание динамических древовидных опросов, прохождение и сохранение результатов.
+ Создавать вопросы и ответы, а также связь между ними с переходом к следующему вопросу в административной панели.
+ Проходить опрос
+ Просмотреть итоговые результаты. (Требуется доработка, так как эксперементировал с сохранением части данных не в базе данных, а на сервере).
___
### Маршруты:

+ Страница с опросом:
```angular2html
http://localhost:8000/
```
+ Административная панель для создания опросов:
```angular2html
http://localhost:8000/admin
```
