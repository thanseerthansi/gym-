from django.contrib import admin

from coachapp.models import CustomerDetailsModel, Diet_PlanModel, ExerciseModel, ExerciseTypeModel, ScheduleModel

# Register your models here.
admin.site.register(ExerciseTypeModel)
admin.site.register(Diet_PlanModel)
admin.site.register(ScheduleModel)
admin.site.register(ExerciseModel)
admin.site.register(CustomerDetailsModel)