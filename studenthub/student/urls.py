from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import student, course , StudentListView , CourseListView, StudentCreatortListView, CourseCreatorListView,\
 CoursetListCreateView, StudentListCreateView, CourseViewSet

urlpatterns = [
    path("student/", student, name="student"),
    path("course/", course, name="course"),
    path("list/", StudentListView.as_view(), name="StudentListView"),
    path("courses/list/", CourseListView.as_view(), name="CourseListView"),
    path("post/", StudentCreatortListView.as_view(), name="StudentCreatortListView"),
    path("courses/post/", CourseCreatorListView.as_view(), name="CourseCreatorListView"),
    path("post/course/", CoursetListCreateView.as_view(), name="CoursetListCreateView"),
    path("post/student/", StudentListCreateView.as_view(), name="StudentListCreateView"),
    path("post/student/", StudentListCreateView.as_view(), name="StudentListCreateView"),
]

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
urlpatterns += router.urls