from loginapp.models import UserDetails
from managerapp.models import *
from managerapp.seralizers import CustomerSeralizers
from rest_framework import serializers
from coachapp.models import CustomerDetailsModel, Diet_PlanModel, ExerciseModel, ExerciseTypeModel, ScheduleModel


class ExerciseTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExerciseTypeModel
        fields = "__all__"

class ExerciseSerializers(serializers.ModelSerializer):
    e_type = ExerciseTypeSerializers(many=True)
    class Meta:
        model = ExerciseModel
        fields = "__all__"

class DietPlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Diet_PlanModel
        fields = "__all__"

class ScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = ScheduleModel
        fields = "__all__"
        
class CustomerDetailsSerializers(serializers.ModelSerializer):
    d_plan = serializers.SerializerMethodField()
    customer = serializers.SerializerMethodField()
    schedule = serializers.SerializerMethodField()

    class Meta:
        model = CustomerDetailsModel
        fields = "__all__"
    
    def get_customer(self,obj) :
        c_obj = UserDetails.objects.filter(id=obj.customer.id,role="customer")
        c_qs = CustomerSeralizers(c_obj,many=True)
        return c_qs.data
    def get_d_plan(self,obj) :
        d_obj = Diet_PlanModel.objects.filter(id=obj.d_plan.id)
        d_qs = DietPlanSerializers(d_obj,many=True)
        return d_qs.data
    def get_schedule(self,obj) :
        s_obj = ScheduleModel.objects.filter(id=obj.schedule.id)
        s_qs = ScheduleSerializers(s_obj,many=True)
        return s_qs.data