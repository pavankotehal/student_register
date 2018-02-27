from django.shortcuts import render
from .models import Student


def student_list(request):
    students = Student.objects.all()
    students = list(students)
    return render(request, 'register/post_list.html', {'students': students})
