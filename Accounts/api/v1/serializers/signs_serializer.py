from rest_framework import serializers 
from Accounts.models import User, Profile
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=8,)
    password_confirm = serializers.CharField(write_only=True, max_length=8,)

    class Meta:
        model = User
        fields= ['email', 'username', 'password', 'password_confirm']
        extra_kwargs = {
            'email': {'required': False},
            'username': {'required': True},  

        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({'password' : 'passwords do not matched'})
        return attrs
    


    def create(self, validated_data):
        validated_data.pop('password_confirm')

        user = User.objects.create_user(**validated_data)
        return user
    

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')        
        password = attrs.get('password')

        user=authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError('invalid email or passworn')
        

        if not user.is_active:
            raise serializers.ValidationError('user disabled')
        
        attrs['user'] = user

        return attrs