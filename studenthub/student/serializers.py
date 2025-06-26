from rest_framework import serializers
from .models import Student, Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

    def validate_title(self, title):
        list_of_titles = set(["Python", "Java", "C++", "C#"])
        if title in list_of_titles:
            return title
        raise serializers.ValidationError(f"Kurs Tabylbady: {list_of_titles}")
