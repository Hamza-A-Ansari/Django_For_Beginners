# Chapter 11: Using {% extends %} Tag in Django Templates

In this chapter, we'll learn how to use the `{% extends %}` tag in Django templates to create a base template and extend its functionality in other templates using `{% block %}` tags.

## Prerequisites

Before proceeding, ensure you have completed Chapter 10 and have your Django project set up with separate header and footer templates.

## Getting Started

1. **Create Base Template:**

    Create a `base.html` file in your `templates` folder. This file will serve as the base template that other templates will extend. In `base.html`, include the header and footer using the `{% include %}` tag, and define a `{% block %}` tag for the main content area. For example:

    ```html
    <!-- base.html -->
    {% include "header.html" %}

    {% block content %}

    {% endblock %}

    {% include "footer.html" %}
    ```

2. **Extending Base Template:**

    In other templates where you want to use the base template's structure, use the `{% extends %}` tag to inherit from `base.html`. Use `{% block %}` tags to override the content of specific blocks defined in the base template. For example, in your `index.html` and `about.html` files:

    ```html
    <!-- index.html -->
    {% extends "base.html" %}
    {% block content %}
    <!-- Page-specific content here -->
    {% endblock %}

    <!-- about.html -->
    {% extends "base.html" %}
    {% block content %}
    <!-- Page-specific content here -->
    {% endblock %}
    ```

    In these examples, `{% extends "base.html" %}` indicates that the templates (`index.html` and `about.html`) extend the base template defined in `base.html`. The `{% block content %}` tag overrides the content of the `content` block defined in the base template, allowing you to insert page-specific content.

## Next Steps

Congratulations! You've successfully used the `{% extends %}` tag in Django templates to create a base template and extend its functionality in other templates. In the next chapter, we'll explore more advanced techniques for creating dynamic and interactive web pages in Django.

