# Chapter 14: Implementing GET Method in Form in Django

In this chapter, we'll learn how to implement the GET method in a form in Django to retrieve user inputs from the URL parameters.

## Prerequisites

Before proceeding, ensure you have completed Chapter 13 and have your Django project set up with highlighted links and a header template.

## Getting Started

1. **Create Form Template:**

    Create a `form.html` file in your `templates` folder. This file will contain the form elements where users can input data. For example:

    ```html
    <!-- form.html -->
    <form action="{% url 'user_form' %}" method="get">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="text" id="email" name="email"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Submit">
    </form>

    <p>{{ output }}</p>
    ```

    In this example, we have a simple form with inputs for name, email, and password. The form submits data using the GET method to the `user_form` URL.

2. **Update URL Patterns:**

    In your `urls.py` file, add a path for the form view. For example:

    ```python
    urlpatterns = [
        # Other URL patterns
        path("user_form/", views.UserForm, name='user_form'),
    ]
    ```

3. **Create Form View Function:**

    In your `views.py` file, create a view function to handle the form submission and retrieve user inputs using the GET method. For example:

    ```python
    # views.py
    def UserForm(request):
        final = ""
        try:
            name = request.GET['name']
            email = request.GET['email']
            password = request.GET['password']
            final = f'Your password is {password}'
        except:
            pass
        return render(request, "form.html", {'output' : final})
    ```

    This view function retrieves the user inputs from the GET parameters (`name`, `email`, and `password`) and constructs a message to display in the template.

4. **Display Output in Form Template:**

    In `form.html`, display the output message using Django template syntax. For example:

    ```html
    <!-- form.html -->
    <!-- Form HTML code -->

    <p>{{ output }}</p>
    ```

    The `{{ output }}` variable contains the message constructed in the view function and is displayed below the form.

## Next Steps

Congratulations! You've successfully implemented the GET method in a form in your Django project to retrieve user inputs from the URL parameters. In the next chapter, we'll explore POST method to get data in Django.

