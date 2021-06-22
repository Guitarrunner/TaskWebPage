from django.shortcuts import render
from django.http import HttpResponse

courses = [
    {
        'courseName': 'Pyhton Basics',
        'professor':  'J. Araya',
        'code': 'CE-101'
    },
    {
        'courseName': 'Java Basics',
        'professor':  'J. Araya',
        'code': 'CE-102'
    },
    {
        'courseName': 'Electronics',
        'professor':  'J.P. Sullivan',
        'code': 'CE-201'
    },
    {
        'courseName': 'Semiconductors',
        'professor':  'J.P. Sullivan',
        'code': 'CE-202'
    },
    {
        'courseName': 'Digital Marketing',
        'professor':  'B. Martinez',
        'code': 'CE-203'
    }
    ]

personal_courses = [
    {
        'courseName': 'Java Basics',
        'professor':  'J. Araya',
        'code': 'CE-102'
    },
    {
        'courseName': 'Electronics',
        'professor':  'J.P. Sullivan',
        'code': 'CE-201'
    },
    ]

def mainPage(request):
    context = {
            'mycourses': personal_courses
        }
    return render(request, 'techCourses/mainPage.html',context)

def about(request):
    return render(request, 'techCourses/about.html')

def list(request):
    context = {
            'courses':courses
        }
    return render(request, 'techCourses/list.html',context)

def visionmision(request):
    return render(request, 'techCourses/visionmision.html')

def contact(request):
    return render(request, 'techCourses/contact.html')

def login(request):
    return render(request, 'techCourses/login.html')

def register(request):
    return render(request, 'techCourses/register.html')

def course(request):
    return render(request, 'techCourses/course.html')
