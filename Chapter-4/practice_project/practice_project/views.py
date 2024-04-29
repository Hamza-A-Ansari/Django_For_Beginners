from django.http import HttpResponse

def AboutUs(request):
    return HttpResponse('Hello World')

def Course(request):
    return HttpResponse('This is my Course page')

def CourseDetail(request, courseId):
    return HttpResponse(f'Your Course ID is {courseId}')