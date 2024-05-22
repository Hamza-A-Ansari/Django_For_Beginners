# Chapter 13: Using Highlighted Links in Django

In this chapter, we'll learn how to highlight links in a navigation menu to indicate the current page in a Django project.

## Prerequisites

Before proceeding, ensure you have completed Chapter 12 and have your Django project set up with URL template tags and a header template.

## Getting Started

1. **Update Header Template with Highlighted Links:**

    In your `header.html` file (or wherever your header is included), update the navigation links to dynamically apply an "active" class to the link corresponding to the current page. We'll achieve this by comparing the current page's URL (`request.path`) with the URLs of the navigation links. For example:

    ```html
    <!-- header.html -->
    <base href="/">
    <link rel="stylesheet" type="text/css" href="static/css/h_style.css">
    <div class="header">
        <a href="#default" class="logo">CompanyLogo</a>
        <div class="header-right">
            {% url "home" as h %}
            <a class="{% if request.path == h %} active {% endif %}" href="{{ h }}">Home</a>
            {% url "contact" as c %}
            <a class="{% if request.path == c %} active {% endif %}" href="{{ c }}">Contact</a>
            {% url "about" as a %}
            <a class="{% if request.path == a %} active {% endif %}" href="{{ a }}">About</a>
        </div>
    </div>
    ```

    In this example, `{% if request.path == h %}` checks if the current page's URL matches the URL of the "Home" link (`h`). If they match, the "active" class is applied to the "Home" link, indicating that it is the current page. The same logic applies to the "Contact" and "About" links.

2. **Style the Active Link:**

    In your CSS file (`h_style.css`), style the "active" class to visually highlight the current page link. For example:

    ```css
      /* Style the active/current link*/
  .header a.active {
    background-color: dodgerblue; /* Change color as desired */
    color: white;
     /* Add any other styles for the active link */
    }
    ```

    In this example, we've set the color of the active link text to blue. You can customize this to fit your project's design.

## Next Steps

Congratulations! You've successfully implemented highlighted links in your Django project to indicate the current page in the navigation menu. In the next chapter, we'll explore what are HTTP Request Methods in Django.

