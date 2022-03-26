from django.shortcuts import render
from coachapp.models import CustomerDetailsModel, ExerciseModel
from coachapp.serializers import CustomerDetailsSerializers, ExerciseSerializers
from customerapp.serializers import CustomerGetSerializers, D_planGetSerializers,  ScheduleGetSerializers
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.
class customerGetAPI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerGetSerializers
    def get_queryset(self):
        id = self.request.POST.get('id','')
        try:
            qs = CustomerDetailsModel.objects.all()
            if id : qs=qs.filter(id=id)
            return qs.order_by('-id')
        except Exception as e:
            return Response({"status":False,"message":str(e),})



class D_planGetAPI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = D_planGetSerializers
    def get_queryset(self):
        id = self.request.POST.get('id','')
        try:
            qs = CustomerDetailsModel.objects.all()
            if id : qs=qs.filter(id=id)
            return qs
        except Exception as e:
            return Response({"status":False,"message":str(e),})



class ScheduleGetAPI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ScheduleGetSerializers
    def get_queryset(self):
        id = self.request.POST.get('id','')
        try:
            qs = CustomerDetailsModel.objects.all()
            if id : qs=qs.filter(id=id)
            return qs.order_by('-id')
        except Exception as e:
            return Response({"status":False,"message":str(e),})


class ExerciseGetAPI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    serializer_class = ExerciseSerializers
    def get_queryset(self):
        try:
            qs = ExerciseModel.objects.all()

            return qs
        except Exception as e:
            return Response({"status":False,"message":str(e),})

