from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('announcements/<str:slug>/', views.details, name='details'),
    path('gallery/', views.gallery, name='gallery'),
    path('announcements/', views.announcements, name='announcements'),
    path('posts/', views.post_list, name='post_list'),
]