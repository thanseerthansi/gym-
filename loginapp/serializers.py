from loginapp.models import UserDetails
import rest_framework

from rest_framework import serializers



class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = "__all__"