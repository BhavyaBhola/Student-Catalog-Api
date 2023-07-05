from .models import Student
from .serializer import StudentDataSerializer , TeacherRegisterSerializer , TeacherLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.




class StudentCatalogView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    def post(self , request):
        data = request.data
        serializer = StudentDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        
        return Response(serializer.errors) 
    
    def patch(self,request):

        data = request.data
        obj = Student.objects.get(id=data['id'])
        serializer = StudentDataSerializer(obj,data=data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def delete(self , request):
        
        data = request.data
        obj = Student.objects.get(id=data['id'])
        obj.delete()

        return Response({'message':'Student details have been deleted'})


class ParticularStudentView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    
    def get(self, request , id):
        try:
            student_data = Student.objects.get(id=id)
            serializer = StudentDataSerializer(student_data)
            return Response(serializer.data)
        except:
            return Response({"message":"Student do not exist"})        


class AllStudentView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    def get(self , request):
        queryset = Student.objects.all()
        serializer = StudentDataSerializer(queryset , many=True)
        return Response(serializer.data)



class RegisterView(APIView):
    
    def post(self,request):
        data = request.data
        serializer = TeacherRegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':serializer.errors
            })
        
        serializer.save()

        return Response({"message":"Teacher account created"})
    

class LoginView(APIView):

    def post(self , request):
        data = request.data
        serializer = TeacherLoginSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'status':False,
                'message':serializer.errors
            }) 

        user = authenticate(username = serializer.data['username'] , password = serializer.data['password'])

        if not user:
            return Response({
                'status':False,
                'message': 'invalid credentials'
            })
        
        token , _ = Token.objects.get_or_create(user=user)

        return Response({'message':"user login" , 'token':str(token)})

