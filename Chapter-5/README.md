# Chapter 5: Rendering HTML Page

In this chapter, we'll render an HTML page in our Django project. Rendering HTML pages allows us to display dynamic content to users using templates.

## Prerequisites

Before proceeding, ensure you have completed Chapter 4 and have your Django project set up with dynamic URL routes and views configured.

## Getting Started

1. **Create Templates Folder:**

    Create a `templates` folder in your project directory, alongside your `manage.py` file. This folder will contain your HTML templates.

2. **Set Templates Folder in Settings:**

    Open your `settings.py` file located in your project directory. Update the `TEMPLATES` setting to include the path to your `templates` folder:

    ```python
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [BASE_DIR, "templates"],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]
    ```

3. **Create View Function:**

    In your `views.py` file, create a view function to render the HTML page. For example:

    ```python
    from django.shortcuts import render

    def homepage(request):
        return render(request, "index.html")
    ```

    This function (`homepage`) uses the `render` method to render the `index.html` template.

4. **Update URLs:**

    Open the `urls.py` file within your app directory. Add a new path to map the root URL to the `homepage` view function:

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", views.homepage),
        path("about/", views.AboutUs),
        path("course/", views.Course),
        path("course/<int:courseId>", views.CourseDetail)
    ]
    ```

    In this example, we've added a new path (`""`) to map the root URL to the `homepage` view function, which will render the `index.html` template.

## Next Steps

Congratulations! You've successfully rendered an HTML page in your Django project. In the next chapter, we'll explore passing data from views to templates to render dynamic content.

