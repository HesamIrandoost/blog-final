from ..serializers import ChangePasswordSerializer, SetNewPasswordSerializer, RequestResetPasswordSerializer
from Accounts.models import PasswordResetToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions, generics
from rest_framework.authtoken.models import Token

class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data,
            context={'request':request}            
        )
        if serializer.is_valid():
            request.user.set_password(serializer.validated_data['new_password'])
            request.user.save()

            Token.objects.filter(user=request.user).delete()
            token = Token.objects.get_or_create(user=request.user)
            return Response({
                    'message':'change password successful',
                    'token':token.key
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RequestResetPasswordView(generics.GenericAPIView):
    
    serializer_class = RequestResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"detail": "If email exists, you will receive reset email"},
                status=status.HTTP_200_OK
            )
            
        token = uuid.uuid4().hex
        expires_at = timezone.now() + timedelta(minutes=10)
        PasswordResetToken.objects.create(
            user=user,
            token=token,
            expired_at=expires_at
        )  

        reset_link = self.request.build_absolute_uri(
            f'/api/v1/accounts/reset-password/confirm/?token={token}'
        )

        # sendـreset_password_email.delay(user.email, reset_link , user.full_name)
                
        return Response(
            {"detail": "If email exists, you will receive reset email"},
            status=status.HTTP_200_OK
        )


class SetNewPasswordView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    
    def get(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        if not token:
            return Response({"error": "Token is required"}, status=400)
        from django.utils import timezone        
        try:
            token_obj = PasswordResetToken.objects.get(token=token)
            if token_obj.is_used or token_obj.expired_at < timezone.now():
                return Response({"error": "Token is invalid or expired"}, status=400)
        except PasswordResetToken.DoesNotExist:
            return Response({"error": "Token is invalid"}, status=400)
            
        return Response({
            "message": "Please send POST request with new password",
            "token": token,
            "example": {
                "password": "new_password123",
                "password_confirm": "new_password123"
            }
        })
    
    def post(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        
        if token:
            data = request.data.copy()
            data['token'] = token
        else:
            data = request.data
            
        serializer = SetNewPasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        
        validated_data = serializer.validated_data 
        token_obj = validated_data['token_obj']
        user = token_obj.user
        new_password = validated_data['password']   
        
        user.set_password(new_password)
        user.save()                   
        token_obj.is_used = True
        token_obj.save()
        
        return Response(
            {"message": "Password changed successfully"},
            status=status.HTTP_200_OK)