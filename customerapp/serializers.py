from coachapp.models import CustomerDetailsModel, Diet_PlanModel, ExerciseModel, ScheduleModel
from coachapp.serializers import DietPlanSerializers, ScheduleSerializers
from loginapp.models import UserDetails
from managerapp.models import *
from managerapp.seralizers import CustomerSeralizers
from rest_framework import serializers

class CustomerGetSerializers(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()
    class Meta:
        model = CustomerDetailsModel
        fields = ["customer"]
    def get_customer(self,obj) :
        c_obj = UserDetails.objects.filter(id=obj.customer.id,role="customer")
        c_qs = CustomerSeralizers(c_obj,many=True)
        return c_qs.data


class D_planGetSerializers(serializers.ModelSerializer):
    d_plan = serializers.SerializerMethodField()
    class Meta:
        model = CustomerDetailsModel
        fields = ["d_plan"]
    def get_d_plan(self,obj) :
        d_obj = Diet_PlanModel.objects.filter(id=obj.d_plan.id)
        d_qs = DietPlanSerializers(d_obj,many=True)
        return d_qs.data

        
class ScheduleGetSerializers(serializers.ModelSerializer):
    schedule = serializers.SerializerMethodField()
    class Meta:
        model = CustomerDetailsModel
        fields = ["schedule", "daily_status"]
    def get_schedule(self,obj) :
        c_obj = ScheduleModel.objects.filter(id=obj.schedule.id)
        c_qs = ScheduleSerializers(c_obj,many=True)
        return c_qs.data
# class ExerciseGetSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = ExerciseModel
#         fields ="__all__"
  

    