from rest_framework.views import APIView
from rest_framework.response import Response
from . models import registration
from . serializer import registrationSerializer
from . models import registration
from django.core.mail import send_mail

# Create your views here.
class register(APIView):
   def get(self, request):
    a = registration.objects.all()
    a1 = registrationSerializer(a, many=True)
    return Response(a1.data)

   def post(self, request):
       reg = request.data
       reg1 = registration(user_name=reg["user_name"], ph_no=reg["ph_no"], gmail=reg["ph_no"], password=reg["password"], key="abcde2", is_active=False)
       reg2 = registrationSerializer(data=reg)
       reg2.is_valid()
       subject = "Registered sucessfully"
       message = "please do follow the link to active http://localhost:8000/registration/verifyEmail?key=abcde2"
       send_mail(subject, message, "ashwinis9632@gmail.com", ["shwetha9990@gmail.com"], fail_silently=False)
       reg1.save()
       return Response(reg2.data)

   def put(self, request):
       id = request.GET.get("id")
       id1 = registration.objects.get(id=id)
       reg = request.data
       req2 = registrationSerializer(id1, data=reg)
       req2.is_valid()
       req2.save()
       return Response(reg)
   def delete(self, request):
       id = request.GET.get("id")
       id1 = registration.objects.get(id=id)
       id1.delete()
       return Response("hye u sucessfully deleted")


class verifyEmail_view(APIView):
    def get(self, request):
        key = request.GET.get("key")
        python_obj = registration.objects.filter(key=key)
        python_obj.is_active = True
        json_obj = registrationSerializer(python_obj, many=True)
        return Response(json_obj.data)