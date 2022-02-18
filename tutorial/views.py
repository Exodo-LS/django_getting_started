from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *


# Create your views here.

def index(request):
    lessons = Lesson.objects.all()
    form = LessonForm()
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'lessons': lessons, 'form': form}
    return render(request, 'tutorial/list.html', context)


def updateLesson(request, pk):
    lesson = Lesson.objects.get(id=pk)
    form = LessonForm(instance=lesson)
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'tutorial/update_lesson.html', context)


def deleteLesson(request, pk):
    item = Lesson.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'tutorial/delete.html', context)
