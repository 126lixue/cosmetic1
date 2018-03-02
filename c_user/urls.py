"""Cosmetic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path,include
from c_user.views import *

urlpatterns = [
    path('login',login),
    path('register',register),
    path('reg_hand', register_handle),
    path('login_hand', login_handle),
    path('logout', logout),
    path('checkname',register_exist),
    path('userinfo', user_center_info),
    path('userupdate', userupdate),
    path('c_address',shdz ),
    path('c_account',user_center_info),
    path('c_index',user_center_info),
    path('add_save',add_save),
    path('mrdz',mrdz),
    path('scdz',scdz),
    path('bjdz',bjdz),



]
