"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',user_views.home,name='home'),
    path('register/',user_views.register,name='register'),
    path('profile/',user_views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path('about1/',user_views.about1,name='about1'),
    path('table1/',user_views.table1,name='table1'),
    path('calendar1/',user_views.calendar1,name='calendar1'),
    path('',include('blog.urls')),
    path('about1/index',user_views.index,name='about1/index'),
    path('table1/about1/',user_views.about1,name='table1/about1/'),
    path('table1/about1/home3/',user_views.home3,name='table1/about1/home3/'),
    path('table1/about1/hi',user_views.setleaves,name="table1/about1/hi"),
    path('hi',user_views.hi,name='hi')
    
    
]
