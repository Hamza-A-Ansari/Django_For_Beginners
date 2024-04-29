# Chapter 4: Adding Dynamic URL Routes

In this chapter, we'll enhance our Django project by adding a dynamic URL route. Dynamic URL routes allow us to capture variable data from the URL and pass it to our view functions.

## Prerequisites

Before proceeding, ensure you have completed Chapter 3 and have your Django project set up with views and URLs configured.

## Getting Started

1. **Update Views:**

    Open your `views.py` file within your app directory. Add the following view function to handle dynamic URLs:

    ```python
    from django.http import HttpResponse

    def CourseDetail(request, courseId):
        return HttpResponse(f'Your Course ID is {courseId}')
    ```

    This function (`CourseDetail`) takes a request object and the `courseId` as parameters and returns an HTTP response displaying the course ID.

2. **Update URLs:**

    Open the `urls.py` file within your app directory. Add a new path to map the dynamic URL route to the `CourseDetail` view function:

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("about/", views.AboutUs),
        path("course/", views.Course),
        path("course/<int:courseId>", views.CourseDetail)
    ]
    ```

    In this example, we've added a new path (`"course/<int:courseId>"`) that captures an integer value (`courseId`) from the URL and passes it to the `CourseDetail` view function.

## Next Steps

Congratulations! You've successfully added a dynamic URL route to your Django project. In the next chapter, we'll explore how to render dynamic content using templates in our views.

