# Chapter 12: Using URL Template Tags in Django

In this chapter, we'll learn how to use URL template tags in Django templates to dynamically generate URLs for views defined in our URLconf.

## Prerequisites

Before proceeding, ensure you have completed Chapter 11 and have your Django project set up with the base template and extended templates.

## Getting Started

1. **Update URL Patterns with Name Variables:**

    In your `urls.py` file, update the URL patterns with name variables using the `name` parameter. This allows you to reference the URLs by their names in the templates. For example:

    ```python
    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", views.homepage, name='home'),
        path("about/", views.AboutUs, name='about'),
        path("course/", views.Course),
        path("contact/", views.ContactUs, name='contact'),
        path("course/<int:courseId>", views.CourseDetail)
    ]
    ```

2. **Update Header Template with URL Template Tags:**

    In your `header.html` file (or wherever your header is included), update the links to use URL template tags. Replace the hardcoded URLs with `{% url 'name' %}` template tags, where `'name'` corresponds to the name given to the URL pattern in `urls.py`. For example:

    ```html
    <!-- header.html -->
    <link rel="stylesheet" href="static/css/h_style.css">
    <div class="header">
        <a href="#default" class="logo">CompanyLogo</a>
        <div class="header-right">
            <a class="active" href="{% url 'home' %}">Home</a>
            <a href="{% url 'contact' %}">Contact</a>
            <a href="{% url 'about' %}">About</a>
        </div>
    </div>
    ```

    In this example, `{% url 'home' %}`, `{% url 'contact' %}`, and `{% url 'about' %}` generate the URLs for the home, contact, and about pages, respectively, based on the URL patterns defined in `urls.py`.

## Next Steps

Congratulations! You've successfully used URL template tags in Django templates to dynamically generate URLs for views defined in your URLconf. In the next chapter, we'll explore more advanced techniques to highlight links in Django.

