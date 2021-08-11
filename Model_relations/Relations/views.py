from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import  csrf_exempt
from rest_framework.parsers import JSONParser
from Relations.models import Posts
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


def home(request):
    return render(request,'index.html')

def login_now(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect(wel_user)
        else:
            return render(request,'index.html',{'msg':'invalid login details'})
    else:
        return render(request,'index.html')

def wel_user(request):
    return render(request,'welcome_user.html')


def log_out(request):
    logout(request)
    return redirect(home)

# --------------------------------------------------------------------------------------

def post_list(request,format=None):
    if request.method=="GET":
        post = Posts.objects.all()
        serializer = PostSerializer(post, many =True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method=="POST":
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


def post_detail(request,pk, format=None):
    try:
        post = Posts.objects.get(pk=pk)
    except Posts.DoesNotExists:
        return HttpResponse(status=404)

    if request.method=='GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)

    elif request.method=='PUT':
        data =JSONParser().parse(request)
        serializer = PostSerializer(post,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        post.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
# ----------------------------------------------------------------------------------------------------------------------
class UserApi(ViewSet):
    def getapi(self,request):
        data = Creators.objects.all().values()
        response = {
            "data":data,
            "success":True,
            "message":"data received"
        }
        status_code=status.HTTP_200_OK
        return Response(response,status_code)

    def createapi(self,request,**data):

        object = Creators.objects.create(**request.data)
        response = {
            "success":True,
            "message":"object created"
        }
        status_code=status.HTTP_200_OK
        return Response(response,status_code)

    def update(self,request,id,**data):
        print(id)
        a=Creators.objects.filter(id=id).update(**request.data)
        if a:
            response = {

                "success":True,
                "message":"update successfully"
            }
            status_code=status.HTTP_200_OK
        else:
            response = {

                "success":False,
                "message":"id not exists"
            }
            status_code=status.HTTP_200_OK
        return Response(response,status_code)

    def delete(self,request,id,**data):
        data = Creators.objects.get(id=id).delete()
        response = {
            "success":True,
            "message":"User deleted"
        }
        status_code=status.HTTP_200_OK
        return Response(response,status_code)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------Many To one-------------------



class Articleobjects(ViewSet):
    def getarticle(self,request):
        object = Aricle.objects.all().values()
        print(object)
        response = {
            "data":object,
            "success":True,
            "message":"data received successfully"
        }
        status_code = status.HTTP_200_OK
        return Response(response,status_code)

    def createaricle(self,request,**data):

        data = request.data
        reporter = data["reporter"]
        try:
            c = Creators.objects.get(id=reporter)
            data["reporter"] = c

            objects = Aricle.objects.create(**request.data)
            response = {
                "success":True,
                "message": " data created successfully"
            }
            status_code = status.HTTP_200_OK

        except Creators.DoesNotExist:
            response= {
                "success":False,
                "message":"Id does not exists in database"
            }
            status_code = status.HTTP_404_NOT_FOUND
        return Response(response,status_code)

    def updatearticle(self,request,id,**data):
        data = request.data
        try:
            x=Aricle.objects.filter(id=id).update(**request.data)
            if x:
                response={
                    "success":True,
                    "message":"data is updated"
                }
                status_code=status.HTTP_200_OK

            else:
                response={
                    "success":False,
                    "message":"Article is not exist"
                }

                status_code=status.HTTP_404_NOT_FOUND
        except:
            pass
        return Response(response,status_code)

    def deletearticle(self,request,id,**data):
        data = Aricle.objects.get(id=id).delete()
        response = {
            "success":True,
            "message":"data deleted"
        }
        status_code = status.HTTP_200_OK
        return Response(response,status_code)


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------Many To Many-------------------------------------------------

class ArticleApi(ViewSet):

    def getarticles(self,request):
        data = Article.objects.all().values()
        response = {
            "data":data,
            "success":True,
            "message":"Data received"
        }
        status_code = status.HTTP_200_OK
        return Response(response,status_code)

    def addarticles(self,request,id):
        data = request.data
        pub_id = id
        try:
            a = Publication.objects.get(id=pub_id)

        except Publication.DoesNotExist:
            response= {
                "success":False,
                "message":"Id does not exists in database"
            }
            status_code = status.HTTP_404_NOT_FOUND
        else:
            publications = data["publications"]
            object =Article.objects.get(id=publications)
            object.publications.add(a)
            response = {
                "success":True,
                "message":"data created successfully"
            }
            status_code = status.HTTP_200_OK

        return Response(response,status_code)

    def createarticles(self,request,**data):

        data = request.data
        print(data)
        publications = data['publications']
        print(publications)
        p = Publication.objects.get(id = publications)

        del data['publications']

        object = Article.objects.create(**request.data)
        object.publications.add(p)
        response = {
            "success":True,
            "message":"Data created"
        }

        status_code = status.HTTP_200_OK
        return Response(response,status_code)


    def updatearticle(self,request,id,**data):
        group_id = id
        data=request.data
        publications = data['publications']
        headline = data['headline']


        article_object =Article.objects.get(id= group_id)
        pub_object = Publication.objects.get(id = publications )

        article_object.publications.clear()
        article_object.publications.add(pub_object)

        x = Article.objects.filter(id=group_id).update(headline=headline)


        response ={
            "success":True,
            "message":"data Updated"
        }
        status_code = status.HTTP_200_OK
        return Response(response,status_code)


    def deletearticles(self,request,id):
        object = Article.objects.get(id=id).delete()
        response={
            "success":True,
            "message":"data deleted"
        }
        status_code = status.HTTP_200_OK
        return Response(response,status_code)

########################################################################################################################



class Userserializer(ViewSet):
    def getuser(self,request):
        serializer = UserdetailSerializer(UserDetails.objects.all(),many=True)
        return Response(serializer.data)


    def createuser(self,request,**data):
        data = request.data
        serializer = UserdetailSerializer(data=data)
        if serializer.is_valid():
            user = UserDetails.objects.create(**request.data)
            response ={
                "success":True,
                "message":"data created"
            }
            status_code=status.HTTP_200_OK
        else:
            response = {
                "success":False,
                "errors":serializer.errors
            }
            status_code=status.HTTP_404_NOT_FOUND
        return Response(response,status_code)


    def updateuser(self,request,id,**data):
        data = request.data
        try:
            use = UserDetails.objects.get(id=id)
            serializer = UserdetailSerializer(use,data=data)
            if serializer.is_valid():
                user = UserDetails.objects.filter(id=id).update(**request.data)

                response ={
                    "success":True,
                    "message":"data updated"
                }
                status_code=status.HTTP_200_OK
            else:
                response = {
                    "success":False,
                    "errors":serializer.errors
                }
                status_code=status.HTTP_404_NOT_FOUND
        except UserDetails.DoesNotExist:
            response= {
                "success":False,
                "mesage":"Id does not exist"
            }
            status_code= status.HTTP_404_NOT_FOUND
        return Response(response,status_code)

    def deleteuser(self,request,id):
        try:
            user = UserDetails.objects.get(id=id).delete()
        except UserDetails.DoesNotExist:
            response={
                "success":False,
                "message":"Id does not exists"
            }
            status_code = status.HTTP_404_NOT_FOUND
        else:
            response={
                "success":True,
                "message":"data deleted"
            }
            status_code = status.HTTP_200_OK

        return Response(response,status_code)








class Createserialize(ViewSet):
    def create(self,request,**data):
        data = request.data.dict()
        print(data)
        serializer = WorkingSerializer(data = data)
        if serializer.is_valid():
            user =data['user']
            u = User.objects.get(id=user)
            data["user"] = u

            obj = Working.objects.create(**data)
            response = {
                "success":True,
                "message":"successful"
            }
            status_code = status.HTTP_200_OK
        else:
            response = {
                "success":False,
                "errors":serializer.errors
            }
            status_code =status.HTTP_404_NOT_FOUND
        return Response(response,status_code)

    def updateworking(self,requeset,id,**data):
        data = requeset.data.dict()
        print(data)
        user = Working.objects.get(id=id)
        obj = User.objects.get(id=id)

        serializer = WorkingSerializer(user,data)
        if serializer.is_valid():
            object = Working.objects.filter(id=id).update(**requeset.data)

            response = {
                "success" : True,
                "message" : "Data updated"
            }
            status_code = status.HTTP_200_OK
        else:
            response = {
                "success" : False,
                "errors" : serializer.errors
            }
            status_code = status.HTTP_404_NOT_FOUND
        return Response(response,status_code)















