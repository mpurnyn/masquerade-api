# Django API for Masquerade

## Project initialization steps
the following steps were taken
1. creating a venv with `python -m venv .env`
2. download postgres and install it with superuser password. also install some gui like pgadmin or dbeaver.
3. install packages `django, psycopg[binary], dotenv`
4. start a new django project `django-admin startproject django_site`
5. verify it works `python manage.py runserver`
6. create an app alongside django_site `python manage.py startapp myapp`
7. add a view for the app
8. add a urls.py file and specify some url paths to point to your app
    - The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name.
9.  add a path to the app in the main site urls.py file
    - urls.py notes:
    - The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.
    - You should always use include() when you include other URL patterns. admin.site.urls is the only exception to this.
10. verify it works again
11. set up postgres db in django_site/settings.py. modify the DATABASES default item.
    - make sure to set the owner of the db (using pgadmin) to the username you supply
    - add the .my_pgpass file to the django_site folder alongside the apps and main site
    - add the .pg_service.conf file on windows to the directory specified in the postgres documentation and if that postgres folder in your app settings doesnt exist then you add it yourself.
    - make sure that the user and db match between the files.
12. set the timezone in the settings file
13. create the initial tables (migrations) for the default django project with `python manage.py migrate`
14. add some models to your app models.py file. 
15. add your add to the isntalled_apps in your settings.
16. run this command `python manage.py makemigrations myapp` to generate migrations for your apps new models. django will run the migrations against your db to create the tables.
17. run python manage.py check to check for any problems in the migrations
18. run the migration again 
19. add a __str__() representation for each model
20. test out python manage.py shell to create new entries for the tables
21. add an admin account for the site wth python manage.py createsuperuser
22. start the server and check out the admin site
23. make app models modifyable in admin by registering them in app\admin.py