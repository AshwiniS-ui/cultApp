
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import offers
from . serializer import offersSerializer


# Create your views here.
class offersView(APIView):
    def get(self, request):
        a = offers.objects.all()
        a1 = offersSerializer(a, many=True)
        return Response(a1.data)