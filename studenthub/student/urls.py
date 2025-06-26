from django.urls import path
from .views import student, course


urlpatterns = [
    path("student/", student, name="student"),
    path("course/", course, name="course"),
]
