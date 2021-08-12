from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse
from .models import *
from .serializer import *
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

############ ManyToMany #####################

class Createposts(ViewSet):
    def getpost(self,request):
       response = {
           "success":False,
           "message":"No data found"
       }
       status_code = status.HTTP_404_NOT_FOUND
       object = Posts.objects.all().values()
       response = {
           "data":object,
           "success":True,
           "message":"Data received"
       }
       status_code = status.HTTP_200_OK
       return Response(response,status_code)


    def createdata(self,request,**data):
        data = request.data.dict()
        print(data)
        serializer = Postserializer(data=data)
        if serializer.is_valid():
            # serializer.save()
            user = data['user']
            object = User.objects.get(id =user)
            data['user']=object
            obj = Posts.objects.create(**data)
            response = {
                "success":True,
                "message":"Data created"
            }
            status_code = status.HTTP_200_OK
        else:
            response ={
                "success":False,
                "errors" : serializer.errors
            }
            status_code = status.HTTP_404_NOT_FOUND
        return Response(response,status_code)


    def updateposts(self,request,id,**data):
        data = request.data.dict()


        user_id = id
        serializer = Postserializer(data=data)
        if serializer.is_valid():
            try:
                user = data['user']
                users = User.objects.get(id=user)

                data['user'] = users

                x = Posts.objects.get(id=user_id).id
                print(x)
                object = Posts.objects.filter(id=x).update(**data)
                response = {
                    "success":True,
                    "message":"Data updated"
                }
                status_code = status.HTTP_200_OK
            except Posts.DoesNotExist:
                response= {
                    "success":False,
                    "message":"Id does not exists"

                }
                status_code = status.HTTP_404_NOT_FOUND
        else:
            response = {
                 "success":False,
                 "errors":serializer.errors
            }
            status_code = status.HTTP_404_NOT_FOUND
        return Response(response,status_code)

    def deleteposts(self,request,id):
        user_id = id
        try:
            user = Posts.objects.get(id=id).delete()
            response = {
                "success":True,
                "message":"Data deleted"
            }
            status_code = status.HTTP_200_OK
        except Posts.DoesNotExist:
            response = {
                "success":False,
                "message": "Id does not exists"
            }
            status_code =status.HTTP_404_NOT_FOUND
        return Response(response,status_code)
