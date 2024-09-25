from django.shortcuts import render
from . import models


def faculty(request):
    faculties = models.Faculty.objects.all()
    cxt = {'faculties': faculties}
    return render(request, 'faculty.html', cxt)


def group(request, pk):
    groups = models.Faculty.objects.get(pk=pk)
    cxt = {'groups': groups}
    return render(request, 'group.html', cxt)

def department(request):
    departments = models.Department.objects.all()
    cxt = {'departments': departments}
    return render(request, 'department.html', cxt)

def student(request, pk):
    students = models.Group.objects.get(pk=pk)
    cxt = {'students': students}
    return render(request, 'student.html', cxt)

def students_detail(request, pk):
    students_details = models.Student.objects.get(pk=pk)
    cxt = {'students': students_details}
    return render(request, 'student details.html', cxt)

def subject(request, pk):
    subjects = models.Department.objects.get(pk=pk)
    cxt = {'subjects': subjects}
    return render(request, 'subject.html', cxt)

def just_subjects(request, pk):
    subjects = models.Department.objects.get(pk=pk)
    cxt = {'subjects': subjects}
    return render(request, 'subjects-2', cxt)

def teacher(request, pk):
    teachers = models.Subject.objects.get(pk=pk)
    cxt = {'teachers': teachers}
    return render(request, 'teacher.html', cxt)

def teacher_detail(request, pk):
    teacher_details = models.Teacher.objects.get(pk=pk)
    cxt = {'teachers': teacher_details}
    return render(request, 'teacher details.html', cxt)

