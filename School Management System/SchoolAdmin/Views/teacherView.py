from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from ..models import *
from django.http import JsonResponse,HttpResponse 
from django.conf import settings
from django.core.mail import send_mail
import random
from datetime import datetime

def addTeacher(request):
    if request.method=="POST": 
        isDone = True
      
        for key in request.POST:
            
            if key=="teacher_id":
                pass
            else:
                if request.POST[key]=="":
                    isDone = False
            
        branch_ids = ",".join(str(element) for element in request.POST.getlist("branch_ids"))
       
        if branch_ids=="":
            isDone = False
        try:
            request.FILES['user_image']
        except:
            isDone = False

        if isDone==False:
            return JsonResponse({'success':False,'msg':'Please fill all the required fields'})
        else:
            teacher_id=request.POST['teacher_id']
            if teacher_id!="":
                pass
            else:
                try:
                    user_image1 = request.FILES['user_image']
                except:
                    user_image1 = "profile/default_img.jpg"
                try:
                    users.objects.create(
                        user_role = "Teacher",
                        user_name = request.POST['user_name'],
                        user_email = request.POST['user_email'],
                        user_password = make_password(request.POST['user_password']),
                        user_image = user_image1
                    )
                except:
                    pass

                user_id1 = users.objects.latest('id')
                teacher_birthdate = datetime.strptime(request.POST['teacher_birthdate'], "%d-%m-%Y").strftime("%Y-%m-%d")
                teacher_joindate = datetime.strptime(request.POST['teacher_joindate'], "%d-%m-%Y").strftime("%Y-%m-%d")
            
                Teacher.objects.create(
                    user_id = user_id1,
                    branch_ids = ",".join(str(element) for element in request.POST.getlist("branch_ids")),
                    teacher_name = request.POST['teacher_name'],
                    teacher_gender = request.POST['teacher_gender'],
                    teacher_birthdate = teacher_birthdate,
                    teacher_joindate = teacher_joindate,
                    teacher_qualification = request.POST['teacher_qualification'],
                    teacher_experience = request.POST['teacher_experience'],
                    teacher_address = request.POST['teacher_address'],
                    teacher_mobile = request.POST['teacher_mobile']
                )
            
                return JsonResponse({'success':True,'msg':'Teacher Save Successfully'})
    else:
      all_branch = branch.objects.all()
      response ={
         'all_branch':all_branch
      }
      return render(request,"add-teacher.html",response)
    
def formValidTeacher(request):
    if request.method=="POST":
        isDone = True
      
        for key in request.POST:
            
            if key=="teacher_id":
                pass
            else:
                if request.POST[key]=="":
                    isDone = False
            
        branch_ids = ",".join(str(element) for element in request.POST.getlist("branch_ids"))
       
        if branch_ids=="":
            isDone = False
        try:
            request.FILES['user_image']
        except:
            isDone = False

        if isDone==False:
            return JsonResponse({'success':False})
        else:
            return JsonResponse({'success':True})




