import json

from django.shortcuts import render
from coachapp.models import *
from coachapp.serializers import *
from loginapp.models import *
import rest_framework
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
# Create your views here.
class ExerciseTypeAPI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ExerciseTypeSerializers
    def post(self,request):
        try:
            id = self.request.POST.get('id','')
            t_name = self.request.POST.get('t_name','')
            
            if id :   
                qs_to_modify = ExerciseTypeModel.objects.filter(id=id) 
                if qs_to_modify.count() :
                    obj_to_modify = qs_to_modify.first()
                    p_obj = ExerciseTypeSerializers(obj_to_modify,data=self.request.data,partial=True)
                    msg="successfully modified"
                else:return Response({"status":False,"message":" no record found "})
            else:
                if t_name:
                    qs_to_check = ExerciseTypeModel.objects.filter(t_name=t_name)
                    if qs_to_check.count():
                        return Response({"status":False,"message":"plan already exist"})
                    p_obj = ExerciseTypeSerializers(data=self.request.data,partial=True)
                    msg = "successfully saved"
            p_obj.is_valid(raise_exception=True)
            obj=p_obj.save()
            saved_data=ExerciseTypeSerializers(obj).data
            return Response({
                "status":True,
                "message":msg,
                "saved data":saved_data
            })
        except Exception as e:
            return Response({"status":False,"message":str(e),})
    def get_queryset(self):
        try:
            qs = ExerciseTypeModel.objects.all()
            id = self.request.POST.get('id','')
            t_name = self.request.POST.get('t_name','')
            
            if id: qs = qs.filter(id=id)
            if t_name: qs= qs.filter(t_name__icontains=t_name)

            return qs
        except Exception as e:
            return Response({"status":False,"message":str(e),})
    def delete(self,request):
        try:
            id = self.request.POST.get('id','[]')
            if id=="all":
                ExerciseTypeModel.objects.all().delete()
                return Response({
                    "message":"deleted all data"
                })
            else:
                id = json.loads(id)
                print("id",id)
                ExerciseTypeModel.objects.filter(id__in=id).delete()
                # print("obj",p_obj)
                # p_obj.delete()
                return Response({"status":True,"message":"deleted successfully"})
        except Exception as e:
            return Response({"status":False,"message":str(e),})
class ExerciseAPI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ExerciseSerializers
    def post(self,request):
        try:
            id = self.request.POST.get('id','')
            e_name = self.request.POST.get('e_name','')
            
            if id :   
                qs_to_modify = ExerciseModel.objects.filter(id=id) 
                if qs_to_modify.count() :
                    obj_to_modify = qs_to_modify.first()
                    p_obj = ExerciseSerializers(obj_to_modify,data=self.request.data,partial=True)
                    msg="successfully modified"
                else:return Response({"status":False,"message":" no record found "})
            else:
                if e_name:
                    qs_to_check = ExerciseModel.objects.filter(e_name=e_name)
                    if qs_to_check.count():
                        return Response({"status":False,"message":"plan already exist"})
                    p_obj = ExerciseSerializers(data=self.request.data,partial=True)
                    msg = "successfully saved"
            p_obj.is_valid(raise_exception=True)
            obj=p_obj.save()
            saved_data=ExerciseSerializers(obj).data
            return Response({
                "status":True,
                "message":msg,
                "saved data":saved_data
            })
        except Exception as e:
            return Response({"status":False,"message":str(e),})
    def get_queryset(self):
        try:
            qs = ExerciseModel.objects.all()
            id = self.request.POST.get('id','')
            e_name = self.request.POST.get('e_name','')
            
            if id: qs = qs.filter(id=id)
            if e_name: qs= qs.filter(e_name__icontains=e_name)

            return qs
        except Exception as e:
            return Response({"status":False,"message":str(e),})
    def delete(self,request):
        try:
            id = self.request.POST.get('id','[]')
            if id=="all":
                ExerciseModel.objects.all().delete()
                return Response({
                    "message":"deleted all data"
                })
            else:
                id = json.loads(id)
                print("id",id)
                ExerciseModel.objects.filter(id__in=id).delete()
                # print("obj",p_obj)
                # p_obj.delete()
                return Response({"status":True,"message":"deleted successfully"})
        except Exception as e:
            return Response({"status":False,"message":str(e),})
    def patch(self,request):
        try:
            exerciseid = self.request.POST['exerciseid']
            typeid = self.request.POST['typeid']
            keyword = self.request.POST['keyword']
            t_qs = ExerciseTypeModel.objects.filter(id=typeid)
            if len(t_qs)==0: return Response({"status":False,"message":"type not found"})

            e_qs=ExerciseModel.objects.filter(id=exerciseid)
            if len(e_qs)==0: return Response({"status":False,"message":"exercise not found"})

            e_obj = e_qs[0]
            if keyword=="add":
                e_obj.e_type.add(t_qs[0])
                msg = "type added successfully"
            if keyword=="remove":
                e_obj.e_type.remove(t_qs[0])
                msg = "type removed successfully"
            return Response({
                "status":True,
                "message":msg,
            })
        except Exception as e:
            return Response({"status":False,"msg": str(e),})
class DietAPI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = DietPlanSerializers
    def post(self,request):
        try:
            id = self.request.POST.get('id','')
            d_name = self.request.POST.get('d_name','')
            
            if id :   
                qs_to_modify = Diet_PlanModel.objects.filter(id=id) 
                if qs_to_modify.count() :
                    obj_to_modify = qs_to_modify.first()
                    p_obj = DietPlanSerializers(obj_to_modify,data=self.request.data,partial=True)
                    msg="successfully modified"
                else:return Response({"status":False,"message":" no record found "})
            else:
                if d_name:
                    qs_to_check = Diet_PlanModel.objects.filter(d_name=d_name)
                    if qs_to_check.count():
                        return Response({"status":False,"message":"plan already exist"})
                    p_obj = DietPlanSerializers(data=self.request.data,partial=True)
                    msg = "successfully saved"
                else: return Response({"status":False,"message":"name is required"})
            p_obj.is_valid(raise_exception=True)
            obj=p_obj.save()
            saved_data=DietPlanSerializers(obj).data
            return Response({
                "status":True,
                "message":msg,
                "saved data":saved_data
            })
        except Exception as e:
            return Response({"status":False,"message":str(e),})
    def get_queryset(self):
        try:
            qs = Diet_PlanModel.objects.all()
            id = self.request.POST.get('id','')
            d_name = self.request.POST.get('d_name','')
            
            if id: qs = qs.filter(id=id)
            if d_name: qs= qs.filter(d_name__icontains=d_name)

            return qs
        except Exception as e:
            return Response({"status":False,"message":str(e),})
    def delete(self,request):
        try:
            id = self.request.POST.get('id','[]')
            if id=="all":
                Diet_PlanModel.objects.all().delete()
                return Response({
                    "message":"deleted all data"
                })
            else:
                id = json.loads(id)
                print("id",id)
                Diet_PlanModel.objects.filter(id__in=id).delete()
                # print("obj",p_obj)
                # p_obj.delete()
                return Response({"status":True,"message":"deleted successfully"})
        except Exception as e:
            return Response({"status":False,"message":str(e),})
class ScheduleAPI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ScheduleSerializers
    def post(self,request):
        try:
            id = self.request.POST.get('id','')
            s_name = self.request.POST.get('s_name','')
            
            if id :   
                qs_to_modify = ScheduleModel.objects.filter(id=id) 
                if qs_to_modify.count() :
                    obj_to_modify = qs_to_modify.first()
                    p_obj = ScheduleSerializers(obj_to_modify,data=self.request.data,partial=True)
                    msg="successfully modified"
                else:return Response({"status":False,"message":" no record found "})
            else:
                if s_name:
                    qs_to_check = ScheduleModel.objects.filter(s_name=s_name)
                    if qs_to_check.count():
                        return Response({"status":False,"message":"plan already exist"})
                    p_obj = ScheduleSerializers(data=self.request.data,partial=True)
                    msg = "successfully saved"
                else: return Response({"status":False,"message":"name is required"})
            p_obj.is_valid(raise_exception=True)
            obj=p_obj.save()
            saved_data=ScheduleSerializers(obj).data
            return Response({
                "status":True,
                "message":msg,
                "saved data":saved_data
            })
        except Exception as e:
            return Response({"status":False,"message":str(e),})
    def get_queryset(self):
        try:
            qs = ScheduleModel.objects.all()
            id = self.request.POST.get('id','')
            s_name = self.request.POST.get('s_name','')
            
            if id: qs = qs.filter(id=id)
            if s_name: qs= qs.filter(s_name__icontains=s_name)

            return qs
        except Exception as e:
            return Response({"status":False,"message":str(e),})
    def delete(self,request):
        try:
            id = self.request.POST.get('id','[]')
            if id=="all":
                ScheduleModel.objects.all().delete()
                return Response({
                    "message":"deleted all data"
                })
            else:
                id = json.loads(id)
                print("id",id)
                ScheduleModel.objects.filter(id__in=id).delete()
                # print("obj",p_obj)
                # p_obj.delete()
                return Response({"status":True,"message":"deleted successfully"})
        except Exception as e:
            return Response({"status":False,"message":str(e),})
class CustomerDetailAPI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerDetailsSerializers
    def post(self,request):
        try:
            id = self.request.POST.get('id','')
            d_plan = self.request.POST.get('d_plan','')
            schedule = self.request.POST.get('schedule','')
            customer = self.request.POST.get('customer','')
            if customer:
                c_obj = UserDetails.objects.filter(id=customer)
                try:
                    
                    c_obj =c_obj.first()
                    checkcustomer = CustomerDetailsModel.objects.filter(customer__id=customer)
                    if checkcustomer.count():
                        return Response({"status":False,"message":"customer already exist"})  
                # d_obj = d_obj[0]
                except Exception as e:
                    return Response({"status":False,"message":str(e),})
            print("id",id)
            if d_plan: 
                try:
                    d_obj = Diet_PlanModel.objects.filter(id=d_plan)
                    d_obj=d_obj.first()
                # d_obj = d_obj[0]
                except:return Response({'status':False,"message":"no record found in Diet with given id"})
                # if len(d_obj)==0: return Response({'status':False,"message":"no record found in Diet with givem id"})
            else:print("elsedplan")
            # print("d_obj",d_obj)
            if schedule: 
                try:
                    s_obj = ScheduleModel.objects.filter(id=schedule)
                    s_obj=s_obj.first()
                except: return Response({'status':False,"message":"no record found in workschedule with given id"})
                # if len(s_obj)==0: return Response({'status':False,"message":"no record found in workschedule with givem id"})
            # print("d_obj",s_obj)

            # print("id2",id)
            # if len(d_obj)==0: return Response({'status':False,"message":"no record found in Diet with givem id"})
          
           
            
            if id :   
                qs_to_modify = CustomerDetailsModel.objects.filter(id=id) 
                if qs_to_modify.count() :
                    # print("d_id",qs_to_modify[0].d_plan)
                    # if not d_plan:
                    #     d_obj = qs_to_modify[0].d_plan
                    # # print("d_id",qs_to_modify[0].schedule)
                    #C
                    #     s_obj = qs_to_modify[0].schedule
                    obj_to_modify = qs_to_modify.first()
                    print("d_id",obj_to_modify.d_plan)
                    if not customer: c_obj = obj_to_modify.customer
                    if  d_plan:
                        pass
                    else:
                        d_obj = obj_to_modify.d_plan
                        print("d_on=bj")
                    if schedule: pass
                    else: s_obj = obj_to_modify.schedule
                    print("diet obj",d_obj)
                    print("schedule obj",s_obj)
                    p_obj = CustomerDetailsSerializers(obj_to_modify,data=self.request.data,partial=True)
                    msg="successfully modified"
                else:return Response({"status":False,"message":" no record found "})
            else:
                print("okkk")
                p_obj = CustomerDetailsSerializers(data=self.request.data,partial=True)
                msg = "successfully saved"
            
            p_obj.is_valid(raise_exception=True)
           
            obj=p_obj.save(customer=c_obj,d_plan=d_obj,schedule=s_obj)
 
            saved_data=CustomerDetailsSerializers(obj).data
            return Response({
                "status":True,
                "message":msg,
                "saved data":saved_data
            })
        except Exception as e:
            return Response({"status":False,"message":str(e),})
    def get_queryset(self):
        # data = Token.objects.get(user=self.request.user.id)
        try:
            qs = CustomerDetailsModel.objects.all()
            id = self.request.POST.get('id','')
            name = self.request.POST.get('name','')
            
            if id: qs = qs.filter(id=id)
            if name: qs= qs.filter(customer__username__contains=name)
            # print("qs",qs)
            # print("customer",qs[0].customer.name)
            

            return qs
        except Exception as e:
            return Response({"status":False,"message":str(e),})
    def delete(self,request):
        try:
            id = self.request.POST.get('id','[]')
            if id=="all":
                ScheduleModel.objects.all().delete()
                return Response({
                    "message":"deleted all data"
                })
            else:
                id = json.loads(id)
                print("id",id)
                ScheduleModel.objects.filter(id__in=id).delete()
                # print("obj",p_obj)
                # p_obj.delete()
                return Response({"status":True,"message":"deleted successfully"})
        except Exception as e:
            return Response({"status":False,"message":str(e),}) 
