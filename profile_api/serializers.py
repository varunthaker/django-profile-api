from rest_framework import serializers
from profile_api import models

class HelloSerializer(serializers.Serializer):
    """Name field to test Serializer"""
    name= serializers.CharField(max_length=10)

class UserProfileSerialiser(serializers.ModelSerializer):
    """Serlialise a user profile object"""
    class Meta:
        model = models.UserProfile
        fields  = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style': {'input_type':'password'}
            }
        }
    def create(self, validate_data):
        """Create and validate new user"""
        user = models.UserProfile.objects.create_user(
            email = validate_data['email'],
            name = validate_data['name'],
        )
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password('password')
        
        return super().update(instance, validated_data)