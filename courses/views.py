from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'home.html')

def categories(request):
    categories = Category.objects.all()
    courses = request.GET.get('courses', '')
    if courses:
        category = courses.filter
    context = {'categories': categories}
    return render(request, 'category-list.html', context)

def category(request, pk):
    category = Category.objects.get(id=pk)
    context = {'category': category}
    return render(request, "category.html", context)


def course(request, pk):
    course = Course.objects.get(id=pk)
    context = {'course': course}
    return render(request, "course.html", context)

def courses(request):
    category = request.GET.get('category', '')
    courses = Course.objects.all()
    if category:
        courses = courses.filter(category_id=category)
    context = {
        'courses': courses,
        'category': category
        }
    return render(request, "courses.html", context)