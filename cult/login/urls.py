from  django.urls import path
from . views import loginView

urlpatterns = [
    path(r'getData', loginView.as_view()),
    path(r'createData', loginView.as_view())
]