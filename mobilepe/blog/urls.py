from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home_view, name='blog_home'),
    path('about/', views.about_view, name='blog_about'),
]
