from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from ..models import *
from django.http import JsonResponse,HttpResponse 
from django.conf import settings
from django.core.mail import send_mail
import random

def viewStdSem(request,depart_id):
    select_department = Department.objects.get(id=depart_id)
    all_StdSem = StdSem.objects.filter(department_id=select_department)
    return render(request,"stdsem.html",{'select_department':select_department,'all_StdSem':all_StdSem})


def actionStdSem(request):
    if request.method=="POST":
        if request.POST['stdsem_action']=="addedit":
            stdsem_id=request.POST['stdsem_id']
            if stdsem_id!="":
                try:
                    edit_StdSem = StdSem.objects.get(id=int(stdsem_id))
                    edit_StdSem.StdSem_name = request.POST['StdSem_name']
                    edit_StdSem.StdSem_duration = request.POST['StdSem_duration']
                    edit_StdSem.save()
                    return JsonResponse({'success':True,'msg':"Save Successfully"})
                except:
                    return JsonResponse({'success':False,'msg':"Something Went Wrong"})
            else:
                try:
                    StdSem.objects.create(
                        StdSem_name = request.POST['StdSem_name'],
                        StdSem_duration = request.POST['StdSem_duration'],
                        department_id = Department(id=int(request.POST['department_id'])),
                    )
                    return JsonResponse({'success':True,'msg':"Save Successfully"})
                except:
                    return JsonResponse({'success':False,'msg':"Something Went Wrong"})
        elif request.POST['stdsem_action']=="delete":
            try:
                select_StdSem = StdSem.objects.get(id=int(request.POST['id']))
                select_StdSem.delete()
                return JsonResponse({'success':True,'msg':"Delete Successfully"})
            except:
                return JsonResponse({'success':False,'msg':"Something Went Wrong"})
        elif request.POST['stdsem_action']=="select":
            try:
                select_StdSem = StdSem.objects.get(id=int(request.POST['id']))
                data = {
                    'success':True,
                    'msg':"Fetch Successfully",
                    'id':select_StdSem.id,
                    'StdSem_name':select_StdSem.StdSem_name,
                    'StdSem_duration':select_StdSem.StdSem_duration,
                    'department_id':select_StdSem.department_id_id
                }
                return JsonResponse(data)
            except:
                return JsonResponse({'success':False,'msg':"Something Went Wrong"})
        elif request.POST['stdsem_action']=="status":
            try:
                select_StdSem = StdSem.objects.get(id=int(request.POST['id']))
                select_StdSem.StdSem_status= request.POST['status']
                select_StdSem.save()
                return JsonResponse({'success':True,'msg':"Status Change Successfully"})
            except:
                return JsonResponse({'success':False,'msg':"Something Went Wrong"})

def viewSubject(request,stdsem_id):
    select_stdsem = StdSem.objects.get(id=stdsem_id)
    all_subject = Subject.objects.filter(stdsem_id=select_stdsem)
    return render(request,"view_subject.html",{'select_stdsem':select_stdsem,'all_subject':all_subject})    

def actionSubject(request):
    if request.method=="POST":
        if request.POST['subject_action']=="addedit":
            subject_id=request.POST['subject_id']
            if subject_id!="":
                try:
                    edit_subject = Subject.objects.get(id=int(subject_id))
                    edit_subject.subject_name = request.POST['subject_name']
                    edit_subject.save()
                    return JsonResponse({'success':True,'msg':"Save Successfully"})
                except:
                    return JsonResponse({'success':False,'msg':"Something Went Wrong"})
            else:
                try:
                    Subject.objects.create(
                        subject_name = request.POST['subject_name'],
                        department_id = Department(id=int(request.POST['department_id'])),
                        stdsem_id = StdSem(id=int(request.POST['stdsem_id'])),
                    )
                    return JsonResponse({'success':True,'msg':"Save Successfully"})
                except:
                    return JsonResponse({'success':False,'msg':"Something Went Wrong"})
        elif request.POST['subject_action']=="delete":
            try:
                select_Subject = Subject.objects.get(id=int(request.POST['id']))
                select_Subject.delete()
                return JsonResponse({'success':True,'msg':"Delete Successfully"})
            except:
                return JsonResponse({'success':False,'msg':"Something Went Wrong"})
        elif request.POST['subject_action']=="select":
            try:
                select_Subject = Subject.objects.get(id=int(request.POST['id']))
                data = {
                    'success':True,
                    'msg':"Fetch Successfully",
                    'id':select_Subject.id,
                    'subject_name':select_Subject.subject_name,
                    'department_id':select_Subject.department_id_id,
                    'stdsem_id':select_Subject.stdsem_id_id
                }
                return JsonResponse(data)
            except:
                return JsonResponse({'success':False,'msg':"Something Went Wrong"})
        elif request.POST['subject_action']=="status":
            try:
                select_Subject = Subject.objects.get(id=int(request.POST['id']))
                select_Subject.subject_status= request.POST['status']
                select_Subject.save()
                return JsonResponse({'success':True,'msg':"Status Change Successfully"})
            except:
                return JsonResponse({'success':False,'msg':"Something Went Wrong"})