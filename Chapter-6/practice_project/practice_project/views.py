from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data = {
        'title' : 'Home Page',
        'header' : 'Welcome to my Page'
    }
    return render(request, "index.html", data)

def AboutUs(request):
    return HttpResponse('Hello World')

def Course(request):
    return HttpResponse('This is my Course page')

def CourseDetail(request, courseId):
    return HttpResponse(f'Your Course ID is {courseId}')