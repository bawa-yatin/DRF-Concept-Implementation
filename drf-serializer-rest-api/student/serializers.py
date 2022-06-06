from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200, required=True)
    last_name = serializers.CharField(max_length=200, required=True)
    address = serializers.CharField(max_length=200, required=True)
    roll_number = serializers.IntegerField()
    mobile = serializers.CharField(max_length=10, required=True)

    def validate_address(self, value):
        if len(value) < 7:
            raise serializers.ValidationError("Address cannot be less than 7 characters")
        return value

    def validate(self, value):
        if len(value['first_name']) < 3 or len(value['last_name']) < 3:
            raise serializers.ValidationError("First and Last Name too short!")
        return value

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.address = validated_data.get('address', instance.address)
        instance.roll_number = validated_data.get('roll_number', instance.roll_number)
        instance.mobile = validated_data.get('mobile', instance.mobile)

        instance.save()
        return instance
