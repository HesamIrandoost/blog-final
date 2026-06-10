from rest_framework import serializers 
from Accounts.models import User, Profile
from django.contrib.auth.password_validation import validate_password

# from rest_framework.authtoken.models import Token

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    new_password_confirm = serializers.CharField(write_only=True)

    
    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password_confirm']:
            raise serializers.ValidationError({'new_password' : 'passwords do not match'})
        return attrs
    
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({'old_password' : 'old password do not match'})
        return value
    


class RequestResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    


class SetNewPasswordSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=250)
    password = serializers.CharField(
        write_only=True,
        max_length=128,  
        validators=[validate_password]
    )
    password_confirm = serializers.CharField(
        write_only=True,
        max_length=128
    )
    
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError({
                "password": "Passwords do not match"
            })
        
        from Accounts.models import PasswordResetToken
        from django.utils import timezone
        
        try:
            token_obj = PasswordResetToken.objects.get(
                token=attrs.get('token')
            )
        except PasswordResetToken.DoesNotExist:
            raise serializers.ValidationError(
                {"token": "Token is not valid"}
            )

        if token_obj.expired_at < timezone.now():
            raise serializers.ValidationError(
                {"token": "Token has expired"}
            )

        if token_obj.is_used:
            raise serializers.ValidationError(
                {"token": "Token has already been used"}
            )

        attrs['token_obj'] = token_obj
        return attrs
c