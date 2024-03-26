from ..models import *
from django.http import JsonResponse,HttpResponse 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..Serializers import *

@api_view(['GET'])
def getTeacher(request):
     teacher_obj = Teacher.objects.all()
     serializer = TeacherSerializer(teacher_obj, many=True)
     return Response({"status": "200","data":serializer.data})

@api_view(['POST'])
def insTeacher(request):
     data = request.data
     serializer = TeacherSerializer(data=request.data)
     if not serializer.is_valid():
          return Response({"status": "403","message":"Something Went Wrong","error":serializer.errors})
     
     serializer.save()
     return Response({"status": "200","message":"Save Successfully"})

