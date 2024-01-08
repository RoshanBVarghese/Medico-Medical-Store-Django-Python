from rest_framework import serializers
from medapp.models import Medicines
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    pass1=serializers.CharField(write_only=True)
    pass2= serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['username','email','password','confirm_password']
        extra_kwargs={'password': {'write_only':'True'}}


        def create(self,validated_data):
            user=User.objects.create_user(validated_data)
            return user
        

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medicines
        fields=('name','company','price','dosage')
        