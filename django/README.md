# Django API for Masquerade

## Project initialization steps
the following steps were taken
1. creating a venv with `python -m venv .env`
2. download postgres and install it with superuser password
3. install packages `django, psycopg`
4. start a new django project `django-admin startproject django_site`
5. verify it works `python manage.py runserver`
6. create an app alongside django_site `python manage.py startapp X`
7. add a view for the app
8. add a urls.py file and specify some url paths to point to your app
    - The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name.
9.  add a path to the app in the main site urls.py file
    - urls.py notes:
    - The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.
    - You should always use include() when you include other URL patterns. admin.site.urls is the only exception to this.
10. verify it works again
11. set up postgres db in django_site/settings.py. modify the DATABASES default item.
