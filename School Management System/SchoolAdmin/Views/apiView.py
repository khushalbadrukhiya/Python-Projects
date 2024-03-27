from ..models import *
from django.http import JsonResponse,HttpResponse 
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..Serializers import *
from rest_framework.views import APIView

class TeacherAPI(APIView):
    def get(self, request):
          teacher_obj = Teacher.objects.all()
          serializer = TeacherSerializer(teacher_obj, many=True)
          return Response({"status": "200","data":serializer.data})
    
    def post(self, request):
                data = request.data
                if len(request.FILES)!=0:
                    user_image1 = request.FILES['user_image']
                else:
                    user_image1 = "profile/default_img.jpg"
            
                try:
                    users.objects.create(
                        user_role = "Teacher",
                        user_name = data.get('user_name'),
                        user_email = data.get('user_email'),
                        user_password = make_password(data.get('user_password')),
                        user_image = user_image1
                    )
                except:
                    pass

                user_id1 = users.objects.latest('id')
                teacher_birthdate = data.get('teacher_birthdate')
                teacher_joindate = data.get('teacher_joindate')
            
                Teacher.objects.create(
                    user_id = user_id1,
                    branch_ids = data.get('branch_ids'),
                    teacher_name = data.get('teacher_name'),
                    teacher_gender = data.get('teacher_gender'),
                    teacher_birthdate = teacher_birthdate,
                    teacher_joindate = teacher_joindate,
                    teacher_qualification = data.get('teacher_qualification'),
                    teacher_experience = data.get('teacher_experience'),
                    teacher_salary = data.get('teacher_salary'),
                    teacher_address = data.get('teacher_address'),
                    teacher_mobile = data.get('teacher_mobile')
                )
                return Response({"status": "200","message":"Save Successfully"})       
    
    def put(self, request):
        pass
    
    def patch(self, request):
          try:
               data = request.data
               teacher_obj = Teacher.objects.get(id=data.get('id'))
               serializer = TeacherSerializer(teacher_obj, data=request.data, partial=True)

               user_obj = users.objects.get(id=teacher_obj.user_id_id)
               serializer = UsersSerializer(user_obj, data=request.data, partial=True)

               if not serializer.is_valid():
                    return Response({"status": "403","message":"Something Went Wrong","error":serializer.errors})
               
               serializer.save()
               return Response({"status": "200","message":"Update Successfully"})
          except Exception as e:
                    return Response({"status": "403","message":"Invalid ID"})
    
    def delete(self, request):
          try:
               data = request.data
               teacher_obj = Teacher.objects.get(id=data.get('id'))
               user_obj = users.objects.get(id=teacher_obj.user_id_id)
               user_obj.delete()
               teacher_obj.delete()
               return Response({"status": "200","message":"Delete Successfully"})
          except Exception as e:
                    return Response({"status": "403","message":"Invalid ID"})


# @api_view(['GET'])
# def getTeacher(request):
#      teacher_obj = Teacher.objects.all()
#      serializer = TeacherSerializer(teacher_obj, many=True)
#      return Response({"status": "200","data":serializer.data})

# @api_view(['POST'])
# def insTeacher(request):
    
#      serializer = TeacherSerializer(data=request.data)
#      if not serializer.is_valid():
#           return Response({"status": "403","message":"Something Went Wrong","error":serializer.errors})
     
#      serializer.save()
#      return Response({"status": "200","message":"Save Successfully"})

# @api_view(['POST'])
# def updTeacher(request,id):
#      try:
#         teacher_obj = Teacher.objects.get(id=id)
#         serializer = TeacherSerializer(teacher_obj, data=request.data, partial=True)
#         if not serializer.is_valid():
#             return Response({"status": "403","message":"Something Went Wrong","error":serializer.errors})
     
#         serializer.save()
#         return Response({"status": "200","message":"Update Successfully"})
#      except Exception as e:
#           return Response({"status": "403","message":"Invalid ID"})
     
# @api_view(['POST'])      
# def deleteTeacher(request,id):
#     try:
#         teacher_obj = Teacher.objects.get(id=id)
#         teacher_obj.delete()
#         return Response({"status": "200","message":"Delete Successfully"})
#     except Exception as e:
#           return Response({"status": "403","message":"Invalid ID"})
