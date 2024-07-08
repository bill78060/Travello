from django.contrib import admin
from django.urls import path
from . import views
from travello.views import homepage

urlpatterns = [
    # path('register',views.register_user),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('home',homepage),

]