from rest_framework import serializers 
from Accounts.models import User, Profile
# from rest_framework.authtoken.models import Token

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email' ,read_only=True)
    username = serializers.CharField(source='user.username' ,read_only=True)
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields= ['email', 'username', 'full_name', 'first_name', 'last_name', 'image', 'bio', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def get_full_name(self, obj):
        return obj.get_full_name()