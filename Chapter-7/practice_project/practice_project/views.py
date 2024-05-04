from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data = {
        'title' : 'Home Page',
        'header' : 'Welcome to my Page',
        'course_list' : ['Python', 'Java', 'C Sharp'],
        'student_details' : [
            {'Name' : 'Hamza', 'Phone' : '0333123456'},
            {'Name' : 'Ahmed', 'Phone' : '0315123456'}
        ]
    }
    return render(request, "index.html", data)

def AboutUs(request):
    return HttpResponse('Hello World')

def Course(request):
    return HttpResponse('This is my Course page')

def CourseDetail(request, courseId):
    return HttpResponse(f'Your Course ID is {courseId}')