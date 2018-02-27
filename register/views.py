from django.shortcuts import render
from .models import Student


def student_list(request):
    return render(request, 'register/post_list.html', {})
