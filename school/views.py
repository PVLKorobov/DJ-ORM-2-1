from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def base(request):
    template = 'base.html'
    return render(request, template)


def students_list(request):
    template = 'students_list.html'
    ordering = 'group'

    students = Student.objects.all().order_by(ordering).prefetch_related('teachers')

    context = {'students': students}
    return render(request, template, context=context)