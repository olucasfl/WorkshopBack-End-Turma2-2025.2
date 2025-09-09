from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    users = User.objects.all()
    return render(request, "home.html", {"users": users})

@api_view(['GET'])
def get_users(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_by_nick(request, nick):
    try:
        user = User.objects.get(pk=nick)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):

    if request.method == 'GET':
        
        try:
            if request.GET['user']:
                user_nickname = request.GET['user']
                user = User.objects.get(pk=user_nickname)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        
        new_user = request.data
        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':

        nickname = request.data['user_nickname']

        try:    
            update_user = User.objects.get(pk=nickname)
            print(request.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(update_user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':

        try:
            user_to_delete = User.objects.get(pk=request.data['user_nickname'])
            user_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)