from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth import get_user_model
from stone.core.models import CustomUser, Error


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def to_representation(self, obj):
        return {"email_id": str(obj.id),
                "email": str(obj.email)
                }      


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['email', 'groups']


class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = ['enviroment','level', 'log', 'events']

    def to_representation(self, obj):
        return {"enviroment": str(obj.enviroment),
                "errors_id": str(obj.id),
                "level": str(obj.level),
                "log": str(obj.log),
                "events": obj.events
                }    
       