from django.contrib import admin
from django.urls import path,include
from .views import StudentCatalogView,RegisterView,LoginView

urlpatterns = [
    path('student/' ,StudentCatalogView.as_view() , name="student_view"),
    path('register/' , RegisterView.as_view() , name='register_view'),
    path('login/' , LoginView.as_view() , name='login')
]
