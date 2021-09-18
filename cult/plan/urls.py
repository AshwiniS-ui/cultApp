from django.urls import path
from . views import planView

urlpatterns = [
    path(r'createData', planView.as_view())
    ]