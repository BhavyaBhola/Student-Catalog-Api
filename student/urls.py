from django.contrib import admin
from django.urls import path,include
from .views import StudentCatalogView,RegisterView,LoginView,ParticularStudentView,AllStudentView

urlpatterns = [
    path('student/' ,StudentCatalogView.as_view() , name="student_view"),
    path('register/' , RegisterView.as_view() , name='register_view'),
    path('login/' , LoginView.as_view() , name='login'),
    path('get_student/<int:id>' ,ParticularStudentView.as_view() , name="student_view"),
    path('all_students/' ,AllStudentView.as_view() , name="student_view"),
]
