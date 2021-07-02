# News_Blog

Последовательность действий для запуска приложения:

В Postgresql следует создать базу данных под названием 'news_for_test'

В файле news_blog/news_blog/settings.py, в DATABASES следует указать своё имя и пароль от postgresql

В терминале pycharm следует ввести последовательно следующие команды:

- python -m venv venv (для создания виртуального окружения)
- venv\Scripts\activate.bat (для активации виртуального окружения)
- cd news_blog
- pip install -r requirements.txt (для установки нужных модулей)
- python manage.py makemigrations
- python manage.py migrate
- python manage.py collectstatic
- python manage.py createsuperuser (далее ввести логин и пароль, для дальнейшего входа в админку)
- python manage.py runserver

На этом установка закончена, далее можно перейти в админку (http://127.0.0.1:8000/admin) по логину и паролю, добавить сначала тэги, а затем уже новости.
