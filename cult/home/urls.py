from django.urls import path
from . views import homeView


urlpatterns = [
    path(r'getData', homeView.as_view())
]