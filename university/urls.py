from django.urls import path
from . import views


urlpatterns = [
    path('', views.faculty),
    path('group/<int:pk>', views.group, name='group'),
    path('department', views.department, name='department'),
    path('student/<int:pk>', views.student, name='student'),
    path('student/details/<int:pk>', views.students_detail, name='student_details'),
    path('subjects/<int:pk>', views.subject, name='subject'),
    path('teacher/<int:pk>', views.teacher, name='teacher'),
    path('teacher/details/<int:pk>', views.teacher_detail, name='teacher_details')
]