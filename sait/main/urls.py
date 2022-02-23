from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    #path('about/', include('about.urls')),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('newsportal', views.newsportal, name='newsportal'),
]