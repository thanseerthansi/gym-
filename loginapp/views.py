

from django.contrib.auth.hashers import make_password
# from typing_extensions import Self

from loginapp.models import UserDetails
from loginapp.serializers import UserSerializers
import rest_framework

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.
class UserAPI(ListAPIView):
    serializer_class = UserSerializers
    Authentication_clases = (TokenAuthentication,)
    Permission_classes =(AllowAny,)
    
    def get_queryset(self):
        try:
            qs = UserDetails.objects.all()
            return qs.order_by('-id')
        except Exception as e:
            return Response({"status":False,"message":str(e),})

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
                print("Adding new UserDetails")
                serializer = UserSerializers(data=request.data,partial=True)
                serializer.is_valid(raise_exception=True)
                msg = "Data saved"
                msg = "created new user"
                user_obj = serializer.save(password=make_password(self.request.data['mobile']))

            return Response({
                "status":True,
                "message":msg,
            })
        except Exception as e:
            print(f"Exception occured {e}")

            if user_obj:
                user_obj.delete()
            return Response({"status":True,"message":f"Exception occured {e}"})
    def delete(self,request):
        try:
            id = self.request.POST.get('id','')
            u_obj = UserDetails.objects.filter(id=id)
            if u_obj.count():
                print("obj",u_obj)
                u_obj.delete()
        
                return Response({"status":True,"message":"deleted successfully"})
            else: return Response({"status":False,"message":"No records with given id" })
            
        except Exception as e:
            return Response({"status":False,"message":str(e),})
class WhoAmI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self,request):
        return Response({
            "Status":1,
            "Data":self.request.user.username
        })


        
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        # print(serializer)
        try:
            test = serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']


            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "STATUS":True,
                'token': "Token "+token.key,
                'user_id': user.pk,
                'username': user.username,
                'is_superuser':user.is_superuser,
            })
        except Exception as e:
            return Response({
                "STATUS":False,
                "MESSAGE":"Incorrect Username or Password",
                "excepction":str(e),
            })
class Logout(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
  
    def get(self,request):
        Data = Token.objects.get(user = self.request.user.id)
        Data.delete()
        return Response({"status":True,"message":"logout successfully"})
