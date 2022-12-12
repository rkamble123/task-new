from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from .models import CourseModel,UserCreateModel,TopicsModel
from .serializers import createUserSerializer,TopicSerializer,CourseSerializer 
from django.http import JsonResponse,HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class create_user(View):
    def get(self,request):
        user = UserCreateModel.objects.all()
        serialized_data = createUserSerializer(user,many=True)
        # for i in user:
        #     print(type(i.name))
        #     print(type(i.user_name))
        #     print(type(i.email))
        #     print(type(i.password))
        return JsonResponse(serialized_data.data,safe= False)

    @csrf_exempt
    def post(self,request):
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream_data)
        serializer = createUserSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse({"msg":"Data Created"})
        return HttpResponse({'msg':'Something Went Wrong'})
        


class create_course(View):
    def get(self,request):
        data = CourseModel.objects.all()
        serialized_data = CourseSerializer(data,many=True)
        return JsonResponse(serialized_data.data,safe= False)
    @csrf_exempt
    def post(self,request):
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream_data)
        serializer = CourseSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse({"msg":"Data Created"})
        return HttpResponse({'msg':'Something Went Wrong'})
    

class add_topic(View):
    def get(self,request):
        data = TopicsModel.objects.all()
        serialized_data = TopicSerializer(data,many=True)
        return JsonResponse(serialized_data.data,safe= False)
        
    @csrf_exempt
    def post(self,request):
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream_data)
        serializer = TopicSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse({"msg":"Data Created"})
        return HttpResponse({'msg':'Somethong Went Wrong'})

    