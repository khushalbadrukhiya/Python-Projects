from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from ..models import *
from django.http import JsonResponse,HttpResponse 
from django.conf import settings
from django.core.mail import send_mail
import random
from datetime import datetime
import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q



def addTeacher(request):
    if request.method=="POST":
        teacher_id=request.POST['teacher_id']

        exclude_key = ["teacher_id"]; 
        if teacher_id!="":
            exclude_key.append("user_password")

      
        isDone = True
      
        for key in request.POST:
            
            if "teacher_id" in exclude_key:
                pass
            else:
                if request.POST[key]=="":
                    isDone = False
            
        branch_ids = ",".join(str(element) for element in request.POST.getlist("branch_ids"))
       
        if branch_ids=="":
            isDone = False
        
        if teacher_id=="":
            try:
                request.FILES['user_image']
            except:
                isDone = False

        if isDone==False:
            return JsonResponse({'success':False,'msg':'Please fill all the required fields'})
        else:
           
            if teacher_id!="":
                 teacher_birthdate = datetime.strptime(request.POST['teacher_birthdate'], "%d-%m-%Y").strftime("%Y-%m-%d")
                 teacher_joindate = datetime.strptime(request.POST['teacher_joindate'], "%d-%m-%Y").strftime("%Y-%m-%d")
                 teacher_edit=Teacher.objects.get(id=teacher_id)
                 teacher_edit.branch_ids = branch_ids
                 teacher_edit.teacher_name = request.POST['teacher_name']
                 teacher_edit.teacher_gender = request.POST['teacher_gender']
                 teacher_edit.teacher_birthdate = teacher_birthdate
                 teacher_edit.teacher_joindate = teacher_joindate
                 teacher_edit.teacher_qualification = request.POST['teacher_qualification']
                 teacher_edit.teacher_experience = request.POST['teacher_experience']
                 teacher_edit.teacher_address = request.POST['teacher_address']
                 teacher_edit.teacher_mobile = request.POST['teacher_mobile']
                 id1=teacher_edit.user_id_id
                 user_edit=users.objects.get(id=id1)
                 user_edit.user_name= request.POST['user_name']
                 user_edit.user_email= request.POST['user_email']
 
                 if request.POST['user_password']!="":
                     user_edit.user_password= make_password(request.POST['user_password'])
                
                 if len(request.FILES)!=0:
                    if user_edit.user_image!="profile/default_img.jpg" and user_edit.user_image!="":
                        os.remove(user_edit.user_image.path)
                        user_edit.user_image= request.FILES['user_image']
                    else:
                        user_edit.user_image= request.FILES['user_image']
                
                 user_edit.save() 
                 teacher_edit.save()  
                 return JsonResponse({'success':True,'msg':'Teacher Save Successfully'})
            else:
                if len(request.FILES)!=0:
                    user_image1 = request.FILES['user_image']
                else:
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
    

def teacherList(request):
    all_branch = branch.objects.all()
    response ={
         'all_branch':all_branch
    }
    return render(request,"teachers.html",response)

def pageWithSearch(request):

    id = request.POST.get('id')
    teacher_name = request.POST.get('teacher_name')
    teacher_mobile = request.POST.get('teacher_mobile')
    teacher_address = request.POST.get('teacher_address')
    teacher_gender = request.POST.get('teacher_gender')
    branch_ids = request.POST.get('branch_ids')
    
    q_objects = Q()
    
    if id!="":
         q_objects &= Q(id__icontains=id)
    if teacher_name!="":
         q_objects &= Q(teacher_name__icontains=teacher_name)
    if teacher_mobile!="":
         q_objects &= Q(teacher_mobile__icontains=teacher_mobile)
    if teacher_address!="":
         q_objects &= Q(teacher_address__icontains=teacher_address)
    if teacher_gender!="":
         q_objects &= Q(teacher_gender__contains=teacher_gender)
    if branch_ids!="":
         q_objects &= Q(branch_ids__icontains=branch_ids)

  
    all_teacher = Teacher.objects.filter(q_objects).order_by('-id')
    # all_teacher = Teacher.objects.all().order_by('-id')

   
    no_of_page = Paginator(all_teacher, 3)

    try:
        page_number = request.POST.get('page_no')
    except:
        page_number=1

    try:
        page_obj = no_of_page.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = no_of_page.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = no_of_page.page(no_of_page.num_pages)

    all_branch = branch.objects.all()
    response ={
        'all_branch':all_branch,
        'all_teacher':page_obj,
        'total_page':range(1, page_obj.paginator.num_pages+1)
    }
    return render(request,"ajax_tbl_teachers.html",response)

def selectTeacher(request,teacher_id):
    select_teacher = Teacher.objects.get(id=teacher_id)
    all_branch = branch.objects.all()
    response ={
        'action':'edit',
        'all_branch':all_branch,
        'select_teacher':select_teacher
    }
    return render(request,"add-teacher.html",response)

def actionTeacher(request):
    if request.method=="POST":
        if request.POST['teacher_action']=="delete":
            try:
                select_Teacher = Teacher.objects.get(id=int(request.POST['id']))
                id1 = select_Teacher.user_id_id
                selectuser=users.objects.get(id=id1)
                if selectuser.user_image!="profile/default_img.jpg" and selectuser.user_image!="":
                    os.remove(selectuser.user_image.path)
                selectuser.delete()
                select_Teacher.delete()
                return JsonResponse({'success':True,'msg':"Delete Successfully"})
            except:
                return JsonResponse({'success':False,'msg':"Something Went Wrong"})




