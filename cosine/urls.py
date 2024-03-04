from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home.html', views.home, name='home.html'),
    path('admin.html', admin.site.urls),
    path('dashboard.html', views.dashboard, name='dashboard.html'),
    path('recruitment.html', views.recruitment, name='recruitment.html'),
    path('results.html', views.results, name='results.html'),
    path('signup.html', views.signup, name='signup'),
    path('jobcard.html', views.jobcard, name='jobcard'),
    path('findee.html', views.findee, name='findee'),


]
