
from django.db import models
from django.contrib.auth.models import AbstractUser


from managerapp.models import  PlanModel


# Create your models here.
class UserDetails(AbstractUser):
    mobile = models.CharField(max_length=20,unique=True,null=False,blank=False,default='')
    role = models.CharField(max_length=20,null=False,blank=False,default='')
    subscriptionplan_id =models.ForeignKey(PlanModel,on_delete=models.DO_NOTHING,null=True,blank=True,default='')
    coach_id = models.ForeignKey('self',on_delete=models.DO_NOTHING,default='',null=True,blank=True)





