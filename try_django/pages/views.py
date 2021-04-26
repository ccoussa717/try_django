from django.http import HttpResponse
from django.shortcuts import render


# Handles your various webpages
def about_view(*args, **kwargs):
    return render(request, "about.html", {})
    

def blog_view(*args, **kwargs):
    return render(request, "blog.html", {})


def contact_view(*args, **kwargs):
    return render(request, "contact.html", {})


def home_view(*args, **kwargs):
    return render(request, "home.html", {})



