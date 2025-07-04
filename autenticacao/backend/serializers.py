from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ['username', 'email', 'perfil', 'password']
    extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['matricula', 'user']           
        extra_kwargs = {'password': {'write_only': True}}

    user = UserSerializer()
    

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)      
        user_serializer.is_valid(raise_exception=True)

        user = user_serializer.save()

        aluno = Aluno.objects.create(user=user, **validated_data)
        return aluno


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['matricula', 'user']           
        extra_kwargs = {'password': {'write_only': True}}

    user = UserSerializer()
    

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)      
        user_serializer.is_valid(raise_exception=True)

        user = user_serializer.save()

        professor = Professor.objects.create(user=user, **validated_data)
        return professor