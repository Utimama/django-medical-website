from django.urls import path
from .views import home_page_view, contact_page_view, error_page_view, blog_page_view

urlpatterns=[
    path('', home_page_view, name="home"),
    path('', contact_page_view, name="Contact"),
    path('', error_page_view, name="404"),
    path('', blog_page_view, name="Blog")
]