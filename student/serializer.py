from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User



class StudentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_name(self, data):

        special_characters = '!@#$%^&*()_+?<>/?=,'

        for c in data:
            if c in special_characters:
                raise serializers.ValidationError('No special characters allowed in student name')

        return data
    

class TeacherRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()    


    def validate(self , data):

        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError("Username already exists")
            
        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('Email already exists')
            
        return data

    def create(self , validated_data):
        user = User.objects.create_user(username=validated_data['username'] , email=validated_data['email'] , password=validated_data['password'])
        user.save()    

        return validated_data
    


class TeacherLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()     