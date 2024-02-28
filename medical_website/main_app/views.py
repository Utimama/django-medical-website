from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request,"main/index.html")


def contact_page_view(request):
    return render(request,"main/contact.html")

def error_page_view(request):
    return render(request, "main/404.html")

def blog_page_view(request):
    return render(request, "main/blog-single.html")




