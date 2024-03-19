from django.db import models
import os

# Create your models here.
class users(models.Model):
    user_role = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_image = models.FileField(upload_to="profile/",default="user_default.jpg")
    user_status = models.IntegerField(default=1)


class branch(models.Model):
    user_id = models.ForeignKey(users,on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=100)
    branch_address = models.CharField(max_length=100)


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_status = models.IntegerField(default=1)

class StdSem(models.Model):
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE)
    StdSem_name = models.CharField(max_length=100)
    StdSem_duration = models.CharField(max_length=100)
    StdSem_status = models.IntegerField(default=1)

class Subject(models.Model):
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE)
    stdsem_id = models.ForeignKey(StdSem,on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    subject_status = models.IntegerField(default=1)


class Teacher(models.Model):
    branch_ids = models.CharField(max_length=50)
    teacher_name = models.CharField(max_length=100)
    teacher_gender = models.CharField(max_length=50)
    teacher_birthdate = models.DateField()
    teacher_joindate = models.DateField()
    teacher_qualification = models.CharField(max_length=100)
    teacher_experience = models.CharField(max_length=100)
    teacher_address = models.TextField()
    teacher_mobile = models.CharField(max_length=30)
    teacher_status = models.IntegerField(default=1)
    user_id = models.ForeignKey(users,on_delete=models.CASCADE)

