
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import home
from . serializer import homeSerializer


# Create your views here.
class homeView(APIView):
    def get(self, request):
        a = home.objects.all()
        a1 = homeSerializer(a, many=True)
        return Response(a1.data)