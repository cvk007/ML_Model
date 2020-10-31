from django.contrib import admin
from django.urls import path
from cvk import views

#Django admin customization
admin.site.site_header = "Login to Cvk007"
admin.site.site_title = "Welcome to Cvk007's Dashboard"
admin.site.index_title = "Welcome folk"

urlpatterns = [
    path('', views.retrieveInf, name='retrieveInf'),
    path('about', views.about, name='about'),
    path('retrieveInf', views.retrieveInf, name='retrieveInf'),
]