from functools import partial
import json
from django.shortcuts import render
from loginapp.models import UserDetails
from loginapp.serializers import UserSerializers
from managerapp.models import *
from managerapp.seralizers import *
import rest_framework
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
# Create your views here.
class SubscriptionAPI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = SubscriptionSerializers
    def post(self,requset):
        id = self.request.POST.get('id','')
        p_name = self.request.POST.get('p_name','')
        try:

            if id :
                # if p_name:
                #     qs_to_modify_byname = PlanModel.objects.filter(p_name=p_name) 
                #     if qs_to_modify_byname.count():
                #         obj_to_modify_byname = qs_to_modify_byname.first()    
                qs_to_modify = PlanModel.objects.filter(id=id) 
                if qs_to_modify.count() :
                    obj_to_modify = qs_to_modify.first()
                    
                    # p_obj = SubscriptionSerializers(obj_to_modify_byname,data=self.request.data,partial=True)
                    p_obj = SubscriptionSerializers(obj_to_modify,data=self.request.data,partial=True)
                    msg="successfully modified"
                else:return Response({"status":False,"message":" no record found "})
            else:
                if p_name:
                    qs_to_check = PlanModel.objects.filter(p_name=p_name)
                    if qs_to_check.count():
                        return Response({"status":False,"message":"plan already exist"})
                p_obj = SubscriptionSerializers(data=self.request.data,partial=True)
                msg = "successfully saved"
            p_obj.is_valid(raise_exception=True)
            obj=p_obj.save()
            saved_data=SubscriptionSerializers(obj).data
            return Response({
                "status":True,
                "message":msg,
                "saved data":saved_data
            })
        except Exception as e:
            return Response({"status":False,"message":str(e),})
    def get_queryset(self):
        qs = PlanModel.objects.all()
        try:
            id = self.request.POST.get('id','')
            p_name = self.request.POST.get('p_name','')
            
            if id: qs = qs.filter(id=id)
            if p_name: qs= qs.filter(p_name__icontains=p_name)

            return qs
        except Exception as e:
            return Response({"status":False,"message":str(e),})
    def delete(self,request):
        try:
            id = self.request.POST.get('id','[]')
            if id=="all":
                PlanModel.objects.all().delete()
                return Response({
                    "message":"deleted all data"
                })
            else:
                id = json.loads(id)
                print("id",id)
                p_obj=PlanModel.objects.filter(id__in=id)
                if p_obj.count():
                    print("obj",p_obj)
                    p_obj.delete()
            
                    return Response({"status":True,"message":"deleted successfully"})
                else: return Response({"status":False,"message":"No records with given id" })
        except Exception as e:
            return Response({"status":False,"message":str(e),})
# class CoachAPI(ListAPIView):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     serializer_class = CoachSerializers
#     def post(self,request):
#         print("receved user data",self.request.data)
#         try:
#             id = self.request.POST.get("id",'')
#             if id:
#                 coach_qs = UserDetails.objects.filter(id=id)
#                 serializer = UserSerializers(coach_qs.first(),data=request.data,partial=True)
#                 serializer.is_valid(raise_exception=True)

#                 password =self.request.POST.get('password','')
#                 if password:
#                     msg = "user details and password updated"
#                     coach_obj = serializer.save(password=make_password(password))
#                 else:
#                     msg = "user details updated"
#                     coach_obj = serializer.save()
               
        
#             else:
#                 print("Adding new UserDetails")
#                 serializer = CoachSerializers(data=request.data,partial=True)
#                 print("done ")
#                 serializer.is_valid(raise_exception=True)
#                 print("done",serializer)
#                 msg = "Data saved"
#                 msg = "created new user"
#                 print(self.request.data['phone'])
#                 coach_obj = serializer.save(password=(self.request.data['phone']))
#                 # serializer.save()
#                 print("done2",serializer)

#             return Response({
#                     "status":True,
#                     "message":msg,
#                 })
#         except Exception as e:
#             print(f"Exception occured {e}")

#             if coach_obj:

#                 coach_obj.delete()
#             return Response({"status":True,"message":f"Exception occured {e}"})
           
#     # def post(self,request):
#     #     id = self.request.POST.get('id','')
#     #     try:
#     #         if id :
                
#     #             qs_to_modify = CoachModel.objects.filter(id=id) 
#     #             if qs_to_modify.count() :
#     #                 obj_to_modify = qs_to_modify.first()
#     #                 c_obj = CoachSerializers(obj_to_modify,data=self.request.data,partial=True)
#     #                 msg="successfully modified"
#     #             else:return Response({"status":False,"message":" no record found "})
#     #         else:
#     #             c_obj = CoachSerializers(data=self.request.data,partial=True)
#     #             msg = "successfully saved"
#     #         c_obj.is_valid(raise_exception=True)
#     #         obj=c_obj.save()
#     #         saved_data=CoachSerializers(obj).data
#     #         return Response({
#     #             "status":True,
#     #             "message":msg,
#     #             "saved data":saved_data
#     #         })
#     #     except Exception as e:
#     #         return Response({"status":False,"message":str(e),})
#     def get_queryset(self):
#         try:
#             qs = CoachModel.objects.all()
#             id = self.request.POST.get('id','')
#             name = self.request.POST.get('name','')
            
#             if id: qs = qs.filter(id=id)
#             if name: qs= qs.filter(name__icontains=name)

#             return qs
#         except Exception as e: return Response({"status":False,"message":str(e),})
#     def delete(self,request):
#         try:
#             id = self.request.POST.get('id','[]')
#             if id=="all":
#                 CoachModel.objects.all().delete()
#                 return Response({
#                     "message":"deleted all data"
#                 })
#             else:
#                 id = json.loads(id)
#                 print("id",id)
#                 CoachModel.objects.filter(id__in=id).delete()
#                 # print("obj",p_obj)
#                 # p_obj.delete()
#                 return Response({"status":True,"message":"deleted successfully"})
#         except Exception as e:
#             return Response({"status":False,"message":str(e),})
class CoachAPI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CoachSerializers
    def get_queryset(self):
        try:
            qs = UserDetails.objects.filter(role="coach")
            id = self.request.POST.get('id','')
            name = self.request.POST.get('name','')
            
            if id: qs = qs.filter(id=id)
            if name: qs= qs.filter(name__icontains=name)

            return qs.order_by('-id')
        except Exception as e: return Response({"status":False,"message":str(e),}) 

    def post(self,request):
        user_obj= ''
        print("receved user data",self.request.data)


        try:
            id = self.request.POST.get("id",'')
            if id:
                user_qs = UserDetails.objects.filter(id=id)
                serializer = UserSerializers(user_qs.first(),data=request.data,partial=True)
                serializer.is_valid(raise_exception=True)

                password =self.request.POST.get('password','')
                if password:
                    msg = "user details and password updated"
                    user_obj = serializer.save(password=make_password(password))
                else:
                    msg = "user details updated"
                    user_obj = serializer.save()
            else:
                Email_address = self.request.POST.get('email') 
                print("Adding new UserDetails")
                print("email",Email_address)
                serializer = UserSerializers(data=request.data,partial=True)
                serializer.is_valid(raise_exception=True)
                msg = "Data saved"
                msg = "created new user"
                user_obj = serializer.save(password=make_password(self.request.data['mobile']),role="coach")
                # if email:
                #     email = EmailMessage(' new coach ', 'congratulation to new coach', to=[Email_address])
                #     email.send()
                

                send_mail(
                    'Subject here',
                    'congratulation to our new coach.',
                    'gymmanagment720@gmail.com',
                    [Email_address],
                    fail_silently=False,
                )

            return Response({
                "status":True,
                "message":msg,
            })
        except Exception as e:
            print(f"Exception occured {e}")

            if user_obj:
                user_obj.delete()
            return Response({"status":False,"message":f"Exception occured {e}"})


    def delete(self,request):
        try:
            id = self.request.POST.get('id','')
            c_obj = UserDetails.objects.filter(id=id,role="coach")
            if c_obj.count():
                c_obj.delete()
                return Response({"status":True,"message":"deleted successfully"})
            else: return Response({"status":False,"message":"given id not found in coach"})
            
        except Exception as e:
            return Response({"status":False,"message":str(e),})
class CustomerAPI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSeralizers
    # def post(self,request):
        # id = self.request.POST.get('id','')
        # subscriptionplan_id = self.request.POST.get('subscriptionplan_id','')
        # coach_id = self.request.POST.get('coach_id','')
        # plan_qs = PlanModel.objects.filter(id=subscriptionplan_id)
        # try:
            
        #     if len(plan_qs)==0:
        #         return Response({"status":False,"message":"No recoed found in Subscribtion plan with provided id"+subscriptionplan_id})
         
        #     coach_qs = UserDetails.objects.filter(id=coach_id,role="coach")
        #     if len(coach_qs)==0: return Response({"status":False,"message":"No record found in coach with provided id"+coach_id})
        # except Exception as e: return Response({"status":False,"message":str(e),})
        # try:
        #     if id :
                
        #         qs_to_modify = CustomerModel.objects.filter(id=id) 
        #         if qs_to_modify.count() :
        #             obj_to_modify = qs_to_modify.first()
        #             c_obj = CustomerSeralizers(obj_to_modify,data=self.request.data,partial=True)
        #             msg="successfully modified"
        #         else:return Response({"status":False,"message":" no record found "})
        #     else:
        #         c_obj = CustomerSeralizers(data=self.request.data,partial=True)
        #         msg = "successfully saved"
        #     c_obj.is_valid(raise_exception=True)
            
        #     obj=c_obj.save(subscriptionplan_id=plan_qs[0],coach_id=coach_qs[0])
        #     saved_data=CustomerSeralizers(obj).data

        #     return Response({
        #         "status":True,
        #         "message":msg,
        #         "saved data":saved_data
        #     })
        # except Exception as e:
        #     return Response({"status":False,"message":str(e),}) 

            #.........
    # def post(self,request):
    #     print("receved user data",self.request.data)

    #     # try:
    #     id = self.request.POST.get("id",'')
    #     print("aftr id",id)
    #     subscriptionplan_id = self.request.POST.get('subscriptionplan_id','')
    #     coach_id = self.request.POST.get('coach_id','')
        
    #     print("id",id)
    #     # try:
    #     if subscriptionplan_id:
    #         plan_qs = PlanModel.objects.get(id=subscriptionplan_id)
    #         print("okkk")
    #         if len(plan_qs)==0:
    #             return Response({"status":False,"message":"No recoed found in Subscribtion plan with provided id"+subscriptionplan_id})
    #         print("okkk2")       
    #     if coach_id:
    #         coach_qs = UserDetails.objects.get(id=coach_id,role="coach")
    #         if len(coach_qs)==0: return Response({"status":False,"message":"No record found in coach with provided id"+coach_id})
    #     # except Exception as e: return Response({"status":False,"message":str(e),})
    #     if id:
    #         user_qs = UserDetails.objects.get(id=id)
    #         print("user_qs",user_qs)
    #         if not subscriptionplan_id:
    #             user_qs = user_qs.subscriptionplan_id
    #         if not coach_id:
    #             user_qs = user_qs.coach_id
            
    #         serializer = UserSerializers(user_qs,data=request.data,partial=True)
    #         print("serializer if id",serializer)
    #         print("daqta if id",request.data)
    #         serializer.is_valid(raise_exception=True)

    #         password =self.request.POST.get('password','')
    #         if password:
    #             msg = "user details and password updated"
    #             user_obj = serializer.save(password=make_password(password),subscriptionplan_id=plan_qs,coach_id=coach_qs)
    #             print("ifpassuser",user_obj)
                
    #         else:
    #             msg = "user details updated"
    #             user_obj = serializer.save(subscriptionplan_id=plan_qs,coach_id=coach_qs)
    #             print("elsepassuser",user_obj)
    #             print("else serializweer",serializer)
    #     else:
    #         print("Adding new UserDetails")
    #         print("data=request.data",request.data)
    #         serializer = UserSerializers(data=request.data,partial=True)
    #         print("serializer",serializer)
    #         serializer.is_valid(raise_exception=True)
    #         msg = "Data saved"
    #         msg = "created new user"
    #         user_obj = serializer.save(password=make_password(self.request.data['mobile']),subscriptionplan_id=plan_qs,coach_id=coach_qs)
    #         print("elseiduser",user_obj)

    #     return Response({
    #         "status":True,
    #         "message":msg,
    #     })
        # except Exception as e:
        #     print(f"Exception occured {e}")

            # if user_obj:
            #     user_obj.delete()
            # return Response({"status":False,"message":f"Exception occured {e}"})
    # -------------------------------------------------------------------------------------
    def post(self,request):
        print("authe",request.auth)
        user_obj = ''
        print("receved user data",self.request.data)

        try:
            id = self.request.POST.get("id",'')
            subscriptionplan_id = self.request.POST.get('subscriptionplan_id','')
            coach_id = self.request.POST.get('coach_id','')
            if subscriptionplan_id:
                s_qs = PlanModel.objects.filter(id=subscriptionplan_id)
                
                if len(s_qs)==0: return Response({"status":False,"message":"No record found in Subcription plan with provided id"+subscriptionplan_id})
                s_qs=s_qs.first()
            if coach_id:
                c_qs = UserDetails.objects.filter(id=coach_id,role="coach")
                
                if len(c_qs)==0: return Response({"status":False,"message":"No record found in coach with provided id"+subscriptionplan_id})
                c_qs = c_qs.first()

            if id:
                user_qs = UserDetails.objects.filter(id=id)
                    
                serializer = UserSerializers(user_qs.first(),data=request.data,partial=True)
                serializer.is_valid(raise_exception=True)
                if not subscriptionplan_id:
                    s_qs = user_qs[0].subscriptionplan_id
                    print("subscriptionplan_id",s_qs)
                if not coach_id:
                    c_qs = user_qs[0].coach_id
                    print("coach_id",c_qs)
                

                password =self.request.POST.get('password','')
                if password:
                    msg = "user details and password updated"
                    user_obj = serializer.save(password=make_password(password),subscriptionplan_id=s_qs,coach_id=c_qs)
                else:
                    msg = "user details updated"
                    user_obj = serializer.save(subscriptionplan_id=s_qs,coach_id=c_qs)
            else:
                print("Adding new UserDetails")
                serializer = UserSerializers(data=request.data,partial=True)
                serializer.is_valid(raise_exception=True)
                msg = "Data saved"
                msg = "created new user"
                user_obj = serializer.save(password=make_password(self.request.data['mobile']),subscriptionplan_id=s_qs,coach_id=c_qs,role="customer")

            return Response({
                "status":True,
                "message":msg,
            })
        except Exception as e:
            print(f"Exception occured {e}")

            if user_obj:
                user_obj.delete()
            
            return Response({"status":False,"message":f"Exception occured {e}"})
    def get_queryset(self):
        try:
            qs = UserDetails.objects.filter(role="customer")
            id = self.request.POST.get('id','')
            name = self.request.POST.get('username','')
            
            if id: qs = qs.filter(id=id)
            if name: qs= qs.filter(username__icontains=name)

            return qs.order_by('-id')
        except Exception as e: return Response({"status":False,"message":str(e),})
    def delete(self,request):
        try:
            id = self.request.POST.get('id','[]')
            if id=="all":
                UserDetails.objects.filter(role="customer").delete()
                return Response({
                    "message":"deleted all data"
                })
            else:
                id = json.loads(id)
                print("id",id)
                p_obj = UserDetails.objects.filter(id__in=id,role="customer")
                if p_obj.count():
                    print("obj",p_obj)
                    p_obj.delete()
            
                    return Response({"status":True,"message":"deleted successfully"})
                else: return Response({"status":False,"message":"No records with given id" })
                # print("obj",p_obj)
                # p_obj.delete()
                
        except Exception as e:
            return Response({"status":False,"message":str(e),})