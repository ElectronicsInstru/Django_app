from django.contrib import admin
from django.urls import path, include

"""Aqui se añaden las urls del proyecto en la siguiente lista, sigue el patron"""
urlpatterns = [
    path('admin/', admin.site.urls),
]
