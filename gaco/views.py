
from django.contrib.auth.models import update_last_login
from django.core.checks import messages
from django.utils import timezone
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import PFE
from .serializer import UserSerrializer, UserSerializerWithToken  , PFESerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status
import uuid
 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data['first_name'],
            last_name = data['last_name'],
            username = data['username'],
            email = data['email'],
            password = make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user , many =False )
        return Response(serializer.data)
    except : 
        message = {'detail': 'User with this e mail already exist'} 
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializers = UserSerrializer(user, many=False)
    return Response(serializers.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializers = UserSerializerWithToken(user, many=False)
    data = request.data

    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.username = data['username']
    user.email = data['email']

    #if data['password'] != '':
        #password = make_password(data['password'])

    user.save()

    return Response(serializers.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializers = UserSerrializer(users, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getPfes(request):
    pfes = PFE.objects.all()
    serializer = PFESerializer(pfes , many=True)
    return Response(serializer.data)

#worked from the first try BTW
@api_view(['DELETE'])
def delete_pfe(request , pk):
    pfe = PFE.objects.get(id=pk)
    pfe.delete()
    return Response('deleted with succes')

@api_view(['POST'])
def ADD_PFE(request):
    data= request.data
    #try:
    pfe = PFE.objects.create(
                institue = data['institue'],
                anneScolere = data['anneScolere'],
                cin = data['cin'],
                nomEtudian=data['nomEtudian'],
                uniqueID=uuid.uuid4().hex[:6].upper(),
                file = request.FILES['file']
            )
    serializer = PFESerializer( pfe , many=False)
    return Response(serializer.data)
    #except:
     #   message = {'detail': 'cannot create object'}
      #  return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def GET_SINGLE_PFE_by_student(request , pk):
    pfe = PFE.objects.filter(nomEtudian = pk)
    serializer = PFESerializer(pfe , many=True)
    return Response(serializer.data)
@api_view(['GET'])
def GET_SINGLE_PFE_by_institue(request, pk):
    pfe = PFE.objects.filter(institue=pk)
    serializer = PFESerializer(pfe, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def GET_SINGLE_PFE_by_year(request, pk):
    pfe = PFE.objects.filter(anneScolere=pk)
    serializer = PFESerializer(pfe, many=True)
    return Response(serializer.data)
