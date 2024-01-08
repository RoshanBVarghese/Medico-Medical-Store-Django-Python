from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .serializers import MedicineSerializer
from medapp.models import Medicines
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# Create your views here.
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def Login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def Signup(request):
    username = request.data.get("username")
    email = request.data.get("email")
    pass1 = request.data.get("password")
    pass2 = request.data.get("password2")
    if not (username and email and pass1):
        return Response({'error': 'Please provide username,email and password'},
                        status=HTTP_400_BAD_REQUEST)
    if pass1!=pass2:
        return Response({'error': 'passwords are not matching'},status=HTTP_400_BAD_REQUEST)
    if User.objects.filter(username=username).exists():
        return Response({"error":"Username already exists"},status=HTTP_400_BAD_REQUEST)
    if User.objects.filter(email=email).exists():
        return Response({"error":"email id  already taken"},status=HTTP_400_BAD_REQUEST)
    user=User.objects.create_user(username=username,email=email,password=pass1)
    user.save()
    return Response({'success':"user created successfully"},status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])

def Medicinelist(request):
    listt=Medicines.objects.all()
    serializer=MedicineSerializer(listt, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(["POST"])

def Medicinecreate(request):
    serializer=MedicineSerializer(data=request.data)
    if serializer.is_valid():
        listt=serializer.save()
        data_list={
            "Name":listt.name,
            "Company":listt.company,
            "Price":listt.price,
            "Dosage":listt.dosage,
        }
        return Response(data_list,status=HTTP_200_OK)
    else:
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    

@csrf_exempt
@api_view(["PUT"])
def Updatemedicine(request,id):
    listt=Medicines.objects.get(id=id)
    serializer=MedicineSerializer(listt,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=HTTP_200_OK)
    else:
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["DELETE"])
def Deletemedicine(request,id):
    listt=Medicines.objects.get(id=id)
    listt.delete()
    return Response("Deleted")

@csrf_exempt
@api_view(["GET"])
def Searchbar(request):
    search=request.GET.get('search')
    if search:
        listt = Medicines.objects.filter(Q(name__istartswith=search))
        serializer=MedicineSerializer(listt,many=True)
        return Response(serializer.data)
    else:
        return Response(status=HTTP_404_NOT_FOUND)