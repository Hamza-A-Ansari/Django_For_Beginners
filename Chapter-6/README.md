# Chapter 6: Passing Data from View to Template

In this chapter, we'll pass data from a Django view to a template. This allows us to render dynamic content in our HTML pages based on data retrieved or processed in our views.

## Prerequisites

Before proceeding, ensure you have completed Chapter 5 and have your Django project set up with the rendering of HTML pages configured.

## Getting Started

1. **Update View Function:**

    In your `views.py` file, update the view function to pass data to the template. For example:

    ```python
    from django.shortcuts import render

    def homepage(request):
        data = {
            'title': 'Home Page',
            'header': 'Welcome to my Page'
        }
        return render(request, "index.html", data)
    ```

    In this example, we've created a dictionary named `data` containing key-value pairs representing the data we want to pass to the template. We then pass this data dictionary as the third argument to the `render` function.

2. **Update HTML Template:**

    In your `index.html` file within the `templates` folder, update the HTML structure to utilize the passed data. For example:

    ```html
    <html>
        <head>
            <title>{{ title }}</title>
        </head>
        <body>
            <h1>{{ header }}</h1>
        </body>
    </html>
    ```

    In this example, we use template tags (`{{ title }}` and `{{ header }}`) to access the data passed from the view. These template tags will be replaced with the corresponding values when the template is rendered.

## Data Format

- **Dictionary Format (views.py):**

    The data passed from the view to the template is typically structured as a dictionary, where keys represent variable names and values represent the corresponding data to be rendered in the template.

- **Template Tags Format (index.html):**

    In the HTML template, data passed from the view is accessed using template tags enclosed within double curly braces (`{{ }}`). The template tags are replaced with the actual values when the template is rendered.

## Next Steps

Congratulations! You've successfully passed data from a Django view to a template and rendered dynamic content in your HTML page. In the next chapter, we'll explore loop using Django template.

