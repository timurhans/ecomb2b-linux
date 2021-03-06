"""ecomb2b URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views
from django.urls import path
from produtos.views import (login_view,logout_view,product_list_view_drop)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('colecao-<str:colecao>/', colecao_view),
    # path('colecao-<str:colecao>/categoria-<str:categoria>/', categoria_view),
    # path('colecao-<str:colecao>/categoria-<str:categoria>/subcategoria-<str:subcategoria>/', product_list_view),
    path('', product_list_view_drop, name='home'),
    path('login/', login_view,name='login'),
    path('accounts/logout/', logout_view), 
]
