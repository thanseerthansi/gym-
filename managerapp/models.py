
from statistics import mode
from django.db import models

# from loginapp.models import UserDetails

# Create your models here.
class PlanModel(models.Model):
    p_name = models.CharField(max_length=20,null=False,blank=False,unique=True,default='')
    p_price = models.FloatField(default=0.0)
    description = models.TextField()

# class CoachModel(models.Model):
#     name = models.CharField(max_length=20,null=False,blank=False)
#     phone = models.IntegerField(null=False,blank=False)

# class CustomerModel(models.Model):
#     name = models.CharField(max_length=20,null=False,blank=False,default='')
#     phone = models.IntegerField(null=False,blank=False)
#     subscriptionplan_id =models.ForeignKey(PlanModel,on_delete=models.DO_NOTHING,default='')
#     coach_id = models.ForeignKey(UserDetails,on_delete=models.DO_NOTHING,default='',null=True,blank=True)


