from django.shortcuts import render

def home(request):
    return render(request,'home.html',{})

def contact(request):
    return render(request,'contact.html',{})

def pricing(request):
    return render(request,'pricing.html',{})

def about(request):
    return render(request,'about.html',{})

def service(request):
    return render(request,'service.html',{})

def blog(request):
    return render(request,'blog.html',{})

def blog_details(request):
    return render(request,'blog-details.html',{})

