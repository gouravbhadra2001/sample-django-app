from django.contrib import admin
from django.urls import path, include

from home import views

admin.site.site_header = "Gourav's Admin Site Header"
admin.site.site_title = "Gourav's Admin Portal"
admin.site.index_title = "Welcome to Gourav's admin site"

#KpNLS-kj:47E8LW

urlpatterns = [
    
    path("", views.index, name="home"),
    path("login", views.loginUser, name = "login"),
        path("logout", views.logoutUser, name = "logout"),

]
