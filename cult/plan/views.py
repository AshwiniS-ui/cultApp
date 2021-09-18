from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import plan
from .serializer import planSerializer


class planView(APIView):
    def post(self, request):
        a = request.data
        a1 = planSerializer(data=a)
        a1.is_valid()
        a1.save()
        return Response(a)
