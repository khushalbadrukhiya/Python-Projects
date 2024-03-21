from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from ..models import *
from django.http import JsonResponse,HttpResponse 
from django.conf import settings
from django.core.mail import send_mail
import random




# Create your views here.
def index(request):
    return redirect('login')

def login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        msg  = ""

        try:
            
            select_user = users.objects.get(user_email=email)
           
            if check_password(password,select_user.user_password) and select_user.user_status==1:
                request.session['user_id'] = select_user.id
                request.session['is_login'] = True
                request.session['user_role'] = select_user.user_role
                request.session['user_email'] = select_user.user_email
                request.session['user_name'] = select_user.user_name
                request.session['user_image'] = select_user.user_image.url
                return redirect('dashboard')
            else:
                msg = "Wrong Password"
        except:
            msg = "Wrong Email"
        
        return render(request,"login.html",{"msg":msg})
    else:
      
        try:
            if  request.session['is_login']==True:
                return redirect('dashboard')
        except:
            return render(request,"login.html")
        return render(request,"login.html")


def isLogin(request):
     if request.session.get('is_login',False)==False:
         return False
     else:
         return True


def dashboard(request):
   
   
    if request.session.get('user_role','none')=="admin":
        return render(request,"dashboard_admin.html")
    elif request.session.get('user_role','none')=="Branch":
        return render(request,"dashboard_principal.html")
    elif request.session.get('user_role','none')=="teacher":
        return render(request,"dashboard_teacher.html")
    elif request.session.get('user_role','none')=="student":
        return render(request,"dashboard_student.html")
    
def logout(request):
    del request.session['user_id']
    del request.session['user_role']
    del request.session['user_email']
    del request.session['user_name']
    del request.session['is_login']
    return redirect('login')

def forgotPassword(request):
    if request.method=="POST":
        if request.POST['action'] == 'email':
            email = request.POST['email']
            try:
                select_user = users.objects.get(user_email=email)
                global otp
                global cemail
                otp=random.randint(100000,900000)
                cemail = select_user.user_email
                subject = 'Forgot Password'
                message = f'Your OTP IS : {otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [select_user.user_email, ]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,"forgot-password.html",{"page":"otp"})
            except:
                msg = "Email Not Found";
                return render(request,"forgot-password.html",{"msg":msg,"page":"email"})
        elif request.POST['action'] == 'otp':
            eotp = int(request.POST['eotp'])
            if eotp==otp:
                return render(request,"forgot-password.html",{"page":"password"})
            else:
                msg = "Wrong OTP"
                return render(request,"forgot-password.html",{"msg":eotp,"page":"otp"})
        elif request.POST['action'] == 'password':
            npassword = request.POST['npassword']
            cpassword = request.POST['cpassword']
            if npassword == cpassword:
                select_user = users.objects.get(user_email=cemail)
                select_user.user_password=make_password(npassword)
                select_user.save()
                return redirect('login')
            else:
                msg = "New password and confirm Password does not match"
                return render(request,"forgot-password.html",{"msg":msg,"page":"password"})
    else:    
        return render(request,"forgot-password.html",{"page":"email"})

def addbranch(request):

    if request.method=="POST":
        branchid=request.POST['branchid']
        if branchid!="":
            try:
                branch_edit=branch.objects.get(id=branchid)
                branch_edit.branch_name= request.POST['branch_name']
                branch_edit.branch_address= request.POST['branch_address']
            
                id1=branch_edit.user_id_id
                user_edit=users.objects.get(id=id1)
                user_edit.user_name= request.POST['user_name']
                user_edit.user_email= request.POST['user_email']

                if request.POST['user_password']!="":
                    user_edit.user_password= make_password(request.POST['user_password'])
                branch_edit.save()

                if len(request.FILES)!=0:
                    if user_edit.user_image!="profile/default_img.jpg" and user_edit.user_image!="":
                        os.remove(user_edit.user_image.path)
                        user_edit.user_image= request.FILES['user_image']
                    else:
                        user_edit.user_image= request.FILES['user_image']
                
                user_edit.save()

                return JsonResponse({'success':True})
            except:
                return JsonResponse({'success':False})
        else:
            if len(request.FILES)!=0:
                user_image1 = request.FILES['user_image']
            else:
                user_image1 = "profile/default_img.jpg"

          
            try:
                users.objects.create(
                    user_role = "Branch",
                    user_name = request.POST['user_name'],
                    user_email = request.POST['user_email'],
                    user_password = make_password(request.POST['user_password']),
                    user_image = user_image1
                )
            except:
                pass

            user_id1 = users.objects.latest('id')
            branch.objects.create(
                user_id = user_id1,
                branch_name = request.POST['branch_name'],
                branch_address = request.POST['branch_address']   
            )
            return JsonResponse({'success':True})

    else:
        all_branch = branch.objects.all()
        return render(request,"branch.html",{"all_branch":all_branch})

def editBranch(request):
    branchid = request.POST['id']
    selectbranch=branch.objects.get(id=branchid)
    return render(request,"ajax_form_editbranch.html",{"selectbranch":selectbranch,"isedit":1})

def deleteBranch(request):
    branchid = request.POST['id']
    selectbranch=branch.objects.get(id=branchid)
    id1 = selectbranch.user_id_id
    selectuser=users.objects.get(id=id1)
    if selectuser.user_image!="profile/default_img.jpg" and selectuser.user_image!="":
        os.remove(selectuser.user_image.path)
    selectuser.delete()
    selectbranch.delete()
    
    return JsonResponse({'success':True})

def profile(request):
    if request.method=="POST":
        

        if request.POST['oldpassword'] and request.POST['newpassword'] and request.POST['cpassword']:
            select_user = users.objects.get(id=request.session['user_id'])
            pass_msg = ""
            if check_password(request.POST['oldpassword'],select_user.user_password):
                if request.POST['newpassword']==request.POST['cpassword']:
                    select_user.user_password = make_password(request.POST['newpassword'])
                    select_user.save()
                    pass_msg = "Password Change Successfully"
                    return JsonResponse({'success':True,'pass_msg':pass_msg})
                else:
                    pass_msg = "New Password and Confirm Password Does Not Match"
            else:
                pass_msg = "Wrong Old Password"
            return JsonResponse({'success':False,'pass_msg':pass_msg})
    else:
        select_user = users.objects.get(id=request.session['user_id'])
        return render(request,"profile.html",{"select_user":select_user})

def changeProfilePhoto(request):
    if request.method=="POST":
        select_user = users.objects.get(id=int(request.POST['user_id']))
        if len(request.FILES)!=0:
            if select_user.user_image!="profile/default_img.jpg" and select_user.user_image!="":
                os.remove(select_user.user_image.path)
                select_user.user_image= request.FILES['user_image']
            else:
                select_user.user_image= request.FILES['user_image']

            select_user.save()
            select_user = users.objects.get(id=int(request.POST['user_id']))
            request.session['user_image'] = select_user.user_image.url
            return JsonResponse({'success':True,'upload_msg':"Photo Change Successfully"})
        else:
            return JsonResponse({'success':False,'upload_msg':"PLease Select Photo"})

def changeUserStatus(request):
    if request.method=="POST":
        select_user = users.objects.get(id=int(request.POST['user_id']))
        try:
            
            select_user.user_status= request.POST['user_status']
            select_user.save()
            return JsonResponse({'success':True,'msg':"Status Change Successfully"})
        except:
            return JsonResponse({'success':False,'msg':"Something Went Wrong"})
    else:
         return JsonResponse({'success':False,'msg':"Something Went Wrong"})
    
def addDepartment(request):
    if request.method=="POST":
        department_id=request.POST['department_id']
        if department_id!="":
            try:
                department_edit=Department.objects.get(id=department_id)
                department_edit.department_name= request.POST['department_name']
                department_edit.save()
                return JsonResponse({'success':True,'msg':"Department Save Successfully"})
            except:
                return JsonResponse({'success':False,'msg':"Something Went Wrong"})
        else:
            try:
                 Department.objects.create(
                    department_name = request.POST['department_name'],
                )
                 return JsonResponse({'success':True,'msg':"Department Save Successfully"})
            except:
                 return JsonResponse({'success':False,'msg':"Something Went Wrong"})
    else:
         all_department = Department.objects.all()
         return render(request,"department.html",{"all_department":all_department})
    
def changeDepartmentStatus(request):
    if request.method=="POST":
        select_deparment = Department.objects.get(id=int(request.POST['department_id']))
        try:
            
            select_deparment.department_status= request.POST['department_status']
            select_deparment.save()
            return JsonResponse({'success':True,'msg':"Status Change Successfully"})
        except:
            return JsonResponse({'success':False,'msg':"Something Went Wrong"})
        
def deleteDepartment(request):
    if request.method=="POST":
        try:
            select_deparment = Department.objects.get(id=int(request.POST['id']))
            select_deparment.delete()
            return JsonResponse({'success':True,'msg':"Delete Successfully"})
        except:
            return JsonResponse({'success':False,'msg':"Something Went Wrong"})

def selectDepartment(request):
    if request.method=="POST":
        try:
             department_id = request.POST['id']
             selectDepartment=Department.objects.get(id=department_id)
          
             return JsonResponse({'success':True,'msg':"Fetch Successfully",'id':selectDepartment.id,'department_name':selectDepartment.department_name})
        except:
            return JsonResponse({'success':False,'msg':"Something Went Wrong"})
