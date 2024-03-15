from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from ..models import *
from django.http import JsonResponse,HttpResponse 
from django.conf import settings
from django.core.mail import send_mail
import random

def addTeacher(request):
    all_branch = branch.objects.all()
    response ={
       'all_branch':all_branch
    }
    return render(request,"add-teacher.html",response)


