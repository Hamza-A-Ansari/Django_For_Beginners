# Chapter 15: Implementing POST Method in Form in Django

In this chapter, we'll learn how to implement the POST method in a form in Django to securely submit user data to the server.

## Prerequisites

Before proceeding, ensure you have completed Chapter 14 and have your Django project set up with a form template and view function for handling form submissions.

## Getting Started

1. **Update Form Template:**

    Update your `form.html` file to use the POST method and include the CSRF token for security. For example:

    ```html
    <!-- form.html -->
    <form method="POST">
        {% csrf_token %}
        <!-- Form inputs -->
        <input type="submit" value="Submit">
    </form>
    ```

    By using the POST method, the form data will be securely submitted to the server. The `{% csrf_token %}` tag ensures protection against Cross-Site Request Forgery (CSRF) attacks.

2. **Handle Form Submission in Views:**

    In your `views.py` file, update the `UserForm` view function to handle the form submission using the POST method. Retrieve the form data from the `request.POST` dictionary. For example:

    ```python
    # views.py
    def UserForm(request):
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
        except Exception as e:
            print(f"Error: {e}")
        return render(request, "form.html", data)
    ```

    In this example, the view function checks if the request method is POST and retrieves the form data (`name`, `email`, and `password`) from the `request.POST` dictionary.

3. **Display Form Data in Template:**

    Update your `form.html` template to display the form data submitted via the POST method. Use Django template syntax to access the form data. For example:

    ```html
    <!-- form.html -->
    <!-- Form inputs -->

    <p>Name: {{ name }}</p>
    <p>Email: {{ email }}</p>
    <p>Password: {{ password }}</p>
    ```

    This code will display the submitted form data (`name`, `email`, and `password`) below the form inputs.

## Next Steps

Congratulations! You've successfully implemented the POST method in a form in your Django project to securely submit user data to the server. In the next chapter, we'll explore more advanced techniques like Redirection of Pages.

