from django.contrib import admin
from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('home/',views.homepage,name='homepage'),
    path('network/', views.network,name='network'),
    path('suggestion/', views.suggestion,name='suggestion'),
    path('insight/', views.insight,name='insight'),
    path('attachment/', views.attachment,name='attachment'),
    path('gettoken/',views.gettoken,name='gettoken'),
]
