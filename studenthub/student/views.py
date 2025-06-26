from django.shortcuts import render
from .models import Student, Course
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import StudentSerializer, StudentCreatorSerializer, CourseSerializer, CourseCreatorSerializer


@api_view(["GET", "POST"])
def student(request):
    method = request.method

    if method == "GET":
        students = Student.objects.all()
        stud_serializer = StudentSerializer(students, many=True)

        return Response(stud_serializer.data, status=status.HTTP_200_OK)
    elif method == "POST":
        crete_serializer = StudentCreatorSerializer(data=request.data)

        if crete_serializer.is_valid():
            student = crete_serializer.save()

            serializer = StudentCreatorSerializer(student)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(
        {"message": f"Hello this is {method} method type"}, status=status.HTTP_200_OK
    )


@api_view(["GET", "POST"])
def course(request):
    method = request.method

    if method == "GET":
        coursee = Course.objects.all()
        cour_serializer = CourseSerializer(coursee, many=True)

        return Response(cour_serializer.data, status=status.HTTP_200_OK)
    elif method == "POST":
        crete_serializer = CourseCreatorSerializer(data=request.data)

        if crete_serializer.is_valid():
            coursee = crete_serializer.save()

            serializer = CourseCreatorSerializer(course)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"error": f"kurs tabylbady"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(
        {"message": f"Hello this is {method} method type"}, status=status.HTTP_200_OK
    )
