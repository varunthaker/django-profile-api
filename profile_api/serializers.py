from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Name field to test Serializer"""
    name= serializers.CharField(max_length=10)