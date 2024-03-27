from rest_framework import serializers
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    user_id = UsersSerializer()
    class Meta:
        model = Teacher
        # fields = ['id', 'branch_ids', 'teacher_name', 'teacher_gender','user_id']
        # exclude = ['teacher_salary','teacher_mobile','teacher_address'] 
        fields = '__all__'
        # depth = 1


        





    