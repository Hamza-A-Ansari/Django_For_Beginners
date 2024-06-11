# Chapter 17: Implementing 'action' URL in Django

In this chapter, we'll learn how to implement the 'action' URL in a Django form to specify the URL to which the form data should be submitted.

## Prerequisites

Before proceeding, ensure you have completed Chapter 16 and have your Django project set up with form handling, view functions, and page redirection.

## Getting Started

1. **Create Submit Template:**

    Create a new template file named `submit.html` in your `templates` folder. This template will be rendered when the form is successfully submitted. For example:

    ```html
    <!-- submit.html -->
    {% extends "base.html" %}
    {% block content %}
    <html>
        <head>
            <title>{{ title }}</title>
        </head>
        <body>
            <h1>Thank you for submitting the form</h1>
            <p>Your password is {{ password }}</p>
        </body>
    </html>
    {% endblock %}
    ```

    This template extends the base template (`base.html`) and displays a confirmation message along with the submitted password.

2. **Update URL Patterns:**

    In your `urls.py` file, add a path for the `submit` view function. For example:

    ```python
    # urls.py
    urlpatterns = [
        # Other URL patterns
        path("submit/", views.Submit, name='submit'),
    ]
    ```

3. **Create Submit View Function:**

    Create a new view function named `Submit` in your `views.py` file. This function will handle the form submission and render the `submit.html` template with the submitted form data. For example:

    ```python
    # views.py
    def Submit(request):
        data = {}
        try:
            if request.method == "POST":
                name = request.POST.get('name')
                email = request.POST.get('email')
                password = request.POST.get('password')

                data = {
                    'name': name,
                    'email': email,
                    'password': password
                }
                # Render the submit.html template with form data
                return render(request, 'submit.html', data)
        except Exception as e:
            print(f"Error: {e}")
        return render(request, 'submit.html')
    ```

    This view function retrieves the form data from the POST request and renders the `submit.html` template with the submitted data.

4. **Update Form Action URL:**

    Update the `action` attribute of your form in `form.html` to specify the URL to which the form data should be submitted. Use the `{% url %}` template tag to dynamically generate the URL. For example:

    ```html
    <!-- form.html -->
    <form method="POST" action="{% url 'submit' %}">
        <!-- Form inputs -->
        <input type="submit" value="Submit">
    </form>
    ```

    This code specifies that the form data should be submitted to the `submit` URL, which is mapped to the `Submit` view function.

## Next Steps

Congratulations! You've successfully implemented the 'action' URL in a Django form to specify the URL to which the form data should be submitted. In the next chapter, we'll explore more advanced techniques for form handling and user interactions in Django.

