# Chapter 3: Setting Up Views and URLs

In this chapter, we'll set up views and connect them to URLs in your Django project. Views are Python functions that take a web request and return a web response. URLs determine which view function is called for a given request.

## Prerequisites

Before proceeding, ensure you have completed Chapter 2 and have your Django project set up with the database configured and a superuser created.

## Getting Started

1. **Create Views:**

    In your Django project, create a `views.py` file (if not already created) within your app directory. Add the following view functions to this file:

    ```python
    from django.http import HttpResponse

    def AboutUs(request):
        return HttpResponse('Hello World')

    def contactpage(request):
        return HttpResponse('This is my contact page')
    ```

    These functions define the logic for your views. For demonstration purposes, we've created two simple views (`AboutUs` and `contactpage`) that return basic HTTP responses.

2. **Update URLs:**

    Open the `urls.py` file within your app directory (typically located alongside `settings.py`). Import your views and define URL patterns to map to these views. For example:

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("about/", views.AboutUs),
        path("contact/", views.contactpage)
    ]
    ```

    In this example, we've mapped the `/about/` URL to the `AboutUs` view function and the `/contact/` URL to the `contactpage` view function.

## Next Steps

Congratulations! You've successfully set up views and connected them to URLs in your Django project. In the next chapter, we'll explore templates to render dynamic content in our views.

