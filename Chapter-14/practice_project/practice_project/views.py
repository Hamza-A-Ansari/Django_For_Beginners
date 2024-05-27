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
        ],
        'Numbers' : [10,20,30,40,50,60,70]
    }
    return render(request, "index.html", data)

def AboutUs(request):
    return render(request, "about.html")

def Course(request):
    return HttpResponse('This is my Course page')

def CourseDetail(request, courseId):
    return HttpResponse(f'Your Course ID is {courseId}')

def ContactUs(request):
    return render(request, "contact.html")

def UserForm(request):
    final = 0
    try:
        name = request.GET['name']
        email = request.GET['email']
        pas = request.GET['password']
        final = f'Your pass is {pas}'
    except:
        pass
    return render(request, "form.html", {'output' : final})