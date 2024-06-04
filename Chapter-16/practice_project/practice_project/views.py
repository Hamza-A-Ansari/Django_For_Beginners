from django.http import HttpResponse
from django.shortcuts import render, redirect

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
    if request.method=='GET':
        output = request.GET.get('password')
    return render(request, "about.html", {'output':output})

def Course(request):
    return HttpResponse('This is my Course page')

def CourseDetail(request, courseId):
    return HttpResponse(f'Your Course ID is {courseId}')

def ContactUs(request):
    return render(request, "contact.html")

def UserForm(request):
    data = {}
    try:
        if request.method=="POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            pas = request.POST.get('password')

            data = {
                'name' : name,
                'email' : email,
                'password' : pas
        }
        url = f"/about/?password={pas}"
        return redirect(url)
    
    except:
        print("Error")
    return render(request, "form.html", data)