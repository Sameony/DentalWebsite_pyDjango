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

{% csrf_token %} hackers se data bachane ke liye form ke andar dala tha
views me jake if request.method == POST:
	post hamara form me tha, agar waisa kuch hora h to if condition lagadi 

def home(request):
    return render(request,'home.html',{Context dictionary - pass stuff from backend to frontend})

passing variable in django - {{ }}
normal tags {% %}

<from django.core.mail import send_mail> mail send krne ke liye XD

python -m smtpd -n -c DebuggingServer localhost:1025 // dummy mail server smtp debugging wala gmail type check karne ke liye mail ffunction chalra ki ni

send_mail(
            message_name,#<-subject,
             message,#<-message,
             message_email,#sender email
             ['probablynotwtf@gmail.com'], #reciever email
             fail_silently=False,

        )
send mail function if request.method==POST wala


EMAIL_HOST= 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER= ''
EMAIL_HOST_PASSWORD

connecting the dummy server