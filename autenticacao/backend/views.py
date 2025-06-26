from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate, login

# Create your views here.


class AlunoRegistrationView(APIView):
    def post(self, request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlunoLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                token.delete()  # Deleta o token antigo
                token = Token.objects.create(user=user)

            response_data = {
                'token': token.key,
                'username': user.username,
                'perfil': user.perfil,
            }

            if user.perfil == 'aluno':
                aluno = user.aluno  # Assumindo que a relação tem nome "aluno"
                if aluno is not None:
                    # Adiciona os dados do aluno ao response_data
                    aluno_data = AlunoSerializer(aluno).data
                    response_data['data'] = aluno_data

            return Response(response_data)
        else:
            return Response({'message': 'Usuário ou Senha Inválido'}, status=status.HTTP_401_UNAUTHORIZED)