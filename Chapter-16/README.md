# Chapter 16: Implementing Page Redirection in Django

In this chapter, we'll learn how to implement page redirection in a Django project using the `redirect` function.

## Prerequisites

Before proceeding, ensure you have completed Chapter 15 and have your Django project set up with form handling and view functions.

## Getting Started

1. **Import `redirect` Function:**

    First, import the `redirect` function from `django.shortcuts` in your `views.py` file:

    ```python
    # views.py
    from django.shortcuts import render, redirect
    ```

2. **Redirect to Another Page:**

    Update your view function (e.g., `UserForm`) to redirect to another page after form submission. Construct the URL of the page to which you want to redirect, and use the `redirect` function with the URL as an argument. For example:

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
                # Construct URL for redirection
                url = f"/about/?password={password}"
                # Redirect to the specified URL
                return redirect(url)
        except Exception as e:
            print(f"Error: {e}")
        return render(request, "form.html", data)
    ```

    In this example, after processing the form data, the view function redirects the user to the `about` page with the password included in the URL as a query parameter.

3. **Modify Redirected Page Function:**

    If necessary, update the view function for the redirected page (e.g., `AboutUs`) to handle the data passed in the URL. For example:

    ```python
    # views.py
    def AboutUs(request):
        output = None
        if request.method == 'GET':
            output = request.GET.get('password')
        return render(request, "about.html", {'output': output})
    ```

4. **Display Data in Redirected Page Template:**

    Update the template for the redirected page (e.g., `about.html`) to display the data passed in the URL. Use Django template syntax to access the data. For example:

    ```html
    <!-- about.html -->
    <p>Your password is {{ output }}</p>
    ```

    This code will display the password passed in the URL on the `about` page.

## Next Steps

Congratulations! You've successfully implemented page redirection in your Django project using the `redirect` function. In the next chapter, we'll explore HTML Action url in Django.

