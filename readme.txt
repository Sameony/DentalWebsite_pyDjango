source virtual/Scripts/activate
venv activation
deactivate: deactivate ho joayega
django-admin startproject <name>:  manage.py file jaha ho us folder me rehke kaam karna
python manage.py runserver
migrate the database always: python manage.py migrate


python manage.py startapp WebHome
(everything is an app for django, make a website? make an app)
after this, go to the dental settings.py and add the app in the installed apps list

static wala reference dena accha h, but ek hi app h to zaruri ni h

{% load static %} at every html webpage, loads static files
static tag sab css,img,js me lagana (reference) //templating
html static hota h, to backend se connect karte h ham is tag se