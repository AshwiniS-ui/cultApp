from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import login
from . serializer import loginSerializer


# Create your views here.
class loginView(APIView):
    def get(self, request):
        a = login.objects.all()
        a1 = loginSerializer(a, many=True)
        return Response(a1.data)


    def post(self, request):
        log = request.data
        reg1 = loginSerializer(data=log)
        reg1.is_valid()
        reg1.save()
        return Response(log)