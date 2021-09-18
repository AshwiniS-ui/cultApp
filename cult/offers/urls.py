from  django.urls import path
from . views import offersView

urlpatterns = [
    path(r'getData', offersView.as_view())
    ]