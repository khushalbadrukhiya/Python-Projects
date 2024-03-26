from rest_framework import serializers
from .models import *
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        # fields = ['id', 'branch_ids', 'teacher_name', 'teacher_gender','user_id']
        exclude = ['teacher_salary','teacher_mobile','teacher_address'] 
        # fields = '__all__'