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
    
     serializer = TeacherSerializer(data=request.data)
     if not serializer.is_valid():
          return Response({"status": "403","message":"Something Went Wrong","error":serializer.errors})
     
     serializer.save()
     return Response({"status": "200","message":"Save Successfully"})

@api_view(['POST'])
def updTeacher(request,id):
     try:
        teacher_obj = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher_obj, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({"status": "403","message":"Something Went Wrong","error":serializer.errors})
     
        serializer.save()
        return Response({"status": "200","message":"Update Successfully"})
     except Exception as e:
          return Response({"status": "403","message":"Invalid ID"})
     
@api_view(['POST'])      
def deleteTeacher(request,id):
    try:
        teacher_obj = Teacher.objects.get(id=id)
        teacher_obj.delete()
        return Response({"status": "200","message":"Delete Successfully"})
    except Exception as e:
          return Response({"status": "403","message":"Invalid ID"})
