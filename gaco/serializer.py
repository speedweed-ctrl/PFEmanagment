from .models import PFE
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken, Token



class UserSerrializer(serializers.ModelSerializer):

    first_name = serializers.SerializerMethodField(read_only=True)
    last_name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['_id', 'first_name', 'last_name','username', 'email',   'isAdmin']

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get__id(self, obj):
        return obj.id

    def get_first_name(slef, obj):
        first_name = obj.first_name
        if first_name == '':
            first_name = obj.email
        return first_name
    
    def get_last_name(slef, obj):
        last_name = obj.last_name
        if last_name == '':
            last_name = 'unnamed'
        return last_name


class UserSerializerWithToken(UserSerrializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['_id', 'username', 'email',  'isAdmin' ,'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class PFESerializer(serializers.ModelSerializer):
    class Meta:
        model = PFE
        fields = '__all__'

