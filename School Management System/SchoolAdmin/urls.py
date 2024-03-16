"""
URL configuration for SchoolSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from SchoolAdmin.Views import views
from SchoolAdmin.Views import stdSemView
from SchoolAdmin.Views import teacherView



urlpatterns = [
    path('', views.login,name="login"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('logout/', views.logout,name="logout"),
    path('addbranch/', views.addbranch,name="addbranch"),
    path('editBranch/', views.editBranch,name="editBranch"),
    path('deleteBranch/', views.deleteBranch,name="deleteBranch"),
    path('forgotPassword/', views.forgotPassword,name="forgotPassword"),
    path('profile/', views.profile,name="profile"),
    path('changeProfilePhoto/', views.changeProfilePhoto,name="changeProfilePhoto"),
    path('changeUserStatus/', views.changeUserStatus,name="changeUserStatus"),
    path('addDepartment/', views.addDepartment,name="addDepartment"),
    path('changeDepartmentStatus/', views.changeDepartmentStatus,name="changeDepartmentStatus"),
    path('deleteDepartment/', views.deleteDepartment,name="deleteDepartment"),
    path('selectDepartment/', views.selectDepartment,name="selectDepartment"),
    path('viewStdSem/<int:depart_id>', stdSemView.viewStdSem,name="viewStdSem"),

    path('actionStdSem/', stdSemView.actionStdSem,name="actionStdSem"),
    path('viewSubject/<int:stdsem_id>', stdSemView.viewSubject,name="viewSubject"),
    path('actionSubject/', stdSemView.actionSubject,name="actionSubject"),

    path('addTeacher/', teacherView.addTeacher,name="addTeacher"),
    path('formValidTeacher/', teacherView.formValidTeacher,name="formValidTeacher"),
   
    
]
