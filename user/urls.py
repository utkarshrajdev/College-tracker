# """college_tracker URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login, name = 'login'),
    path('login', views.login, name = 'login'),
    path('showcolleges', views.showcolleges, name = 'showcolleges'),
    path('editcollegedetails', views.editcollegedetails, name = 'editcollegedetails'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout, name = 'logout'),
    path('changepassword', views.changepassword, name = 'changepassword'),
    path('search-colleges/', views.CollegeSearchView, name = 'search_colleges'),
    path('savefollowup', views.savefollowup, name = 'savefollowup'),
    path('editprofile', views.editprofile, name = 'editprofile'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('reset_password_set/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_send.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),

]

