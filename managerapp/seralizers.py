from dataclasses import field, fields
from loginapp.serializers import UserSerializers
from rest_framework import serializers
# from managerapp.models import *
from loginapp.models import UserDetails
from managerapp.models import PlanModel



class SubscriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = PlanModel
        fields = "__all__"
# class CoachSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = CoachModel
#         fields = "__all__"
class CoachSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('id','username','mobile','date_joined')

class CustomerSeralizers(serializers.ModelSerializer):
    subscriptionplan_id = serializers.SerializerMethodField()
    coach_id = serializers.SerializerMethodField()
    class Meta:
        model = UserDetails
        fields = "__all__"
   
    def get_subscriptionplan_id(self,obj):
        print("get subscibtion plans id",obj.subscriptionplan_id.id)
        p_obj = PlanModel.objects.filter(id=obj.subscriptionplan_id.id) 
        p_qs = SubscriptionSerializers(p_obj,many=True)
        return p_qs.data  
    def get_coach_id(self,obj):
        c_obj = UserDetails.objects.filter(id=obj.coach_id.id) 
        c_qs = UserSerializers(c_obj,many=True)
        return c_qs.data

# class CoachDetailsSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = CoachDetails
#         fields = "__all__"