from django.db import models
from loginapp.models import UserDetails



# Create your models here.
class ExerciseTypeModel(models.Model):
    t_name = models.CharField(max_length=50,null=False,blank=False)
class Diet_PlanModel(models.Model):
    d_name = models.CharField(max_length=20,null=False,blank=False)
    d_description = models.TextField()

class ScheduleModel(models.Model):
    s_name = models.CharField(max_length=20,null=False,blank=False)
    s_description = models.TextField()
class ExerciseModel(models.Model):
    e_name = models.CharField(max_length=20,null=False,blank=False)
    e_type = models.ManyToManyField(ExerciseTypeModel)

class CustomerDetailsModel(models.Model):
    customer = models.ForeignKey(UserDetails,on_delete=models.CASCADE,default='',null=True)
    d_plan = models.ForeignKey(Diet_PlanModel,on_delete=models.DO_NOTHING,default='',null=True)
    schedule = models.ForeignKey(ScheduleModel,on_delete=models.DO_NOTHING,default='',null=True)
    daily_status = models.TextField()
