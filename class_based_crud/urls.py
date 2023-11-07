"""class_based_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import ListAll, Add, ListSearch, Update, SendMail, SendVideo, SendMesage, ReceiveMessage

urlpatterns = [
    path("list-all/", ListAll.as_view()),
    path("list-all/<int:id>", ListSearch.as_view()),
    path("add/", Add.as_view()),
    path("delete/<int:id>", ListAll.as_view()),
    path("update/<int:id>", Update.as_view()),
    path("send-mail/", SendMail.as_view()),
    path('send-video/', SendVideo.as_view()),
    path('send-message/', SendMesage.as_view()),
    path('receive-message/', ReceiveMessage.as_view())
]
