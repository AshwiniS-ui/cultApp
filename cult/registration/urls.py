from django.contrib import admin

from django.urls import path
from . views import register, verifyEmail_view

urlpatterns = [
    path(r'getData', register.as_view()),
    path(r'createData', register.as_view()),
    path(r'updateData', register.as_view()),
    path(r'deleteData', register.as_view()),
    path(r'verifyEmail', verifyEmail_view.as_view())
]