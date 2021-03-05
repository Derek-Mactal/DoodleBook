from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.registration),
    path('register', views.register),
    path('dashboard', views.dashboard),
    path('admin', views.admin),
    path('profile', views.profile),
    path('edit', views.edit_profile),
    path('admin_edit', views.admin_edit),
    path('logout', views.logout),
    path('login', views.login),
]