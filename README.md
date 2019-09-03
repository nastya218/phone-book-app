# phone-book-app
For the application to work, you need django, python.
At the CMD go to the project directory.
To create a database and migrations, enter the command:python manage.py makemigrations phoneList.
To apply migrations you need to enter the command: python manage.py migrate.
That's all, DB was created.

To create an admin account, enter the command: python manage.py createsuperuser,
and then enter user name : admin, password: admin, and save changes.

To work with the database, enter the command: python manage.py runserver.
