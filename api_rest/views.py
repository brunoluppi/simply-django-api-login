from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .utils import token
from django.conf import settings
import jwt

import uuid

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

@api_view(['POST'])
def user_register(request):
    if request.method == 'POST':
        data = request.data
        if User.objects.filter(user_email=data['user_email']).exists():
            return Response(status=status.HTTP_409_CONFLICT)
        data['user_id'] = str(uuid.uuid4())
        if len(data['user_password']) < 8:
            return Response({'error': 'A senha não pode conter menos de 8 caracteres'}, status=status.HTTP_411_LENGTH_REQUIRED)
        data['user_password'] = make_password(data['user_password'])
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        data = request.data
        user_email = data.get('user_email')
        user_password = data.get('user_password')
        try:
            user = User.objects.get(user_email=user_email)
        except User.DoesNotExist:
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        if check_password(user_password, user.user_password):
            new_token = token.generate_token(user_email)
            user.user_token = new_token
            user.save(update_fields=['user_token'])
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def validate_token(request):
    token = request.data.get('user_token')
    if not token:
        return Response({'error': 'Token é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_email = payload.get('user_email')
        user = User.objects.filter(user_email=user_email).first()
        user_data = UserSerializer(user).data
        user_token = user_data.get('user_token')
        if token != user_token:
            return Response({'error': 'Token inválido'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'valid': True, 'payload': payload}, status=status.HTTP_200_OK)
    except jwt.ExpiredSignatureError:
        return Response({'error': 'Token expirado'}, status=status.HTTP_401_UNAUTHORIZED)
    except jwt.InvalidTokenError:
        return Response({'error': 'Token inválido'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['PUT'])
def modify_user(request):
    if request.method == 'PUT':
        return Response()
    
@api_view(['PUT'])
def forgot_password(request):
    if request.method == 'PUT':
        return Response()
    
@api_view(['DELETE'])
def delete_account(request):
    if request.method == 'DELETE':
        return Response()