from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="homepg"),
    path('contact.html',views.contact, name="contact"),
]
