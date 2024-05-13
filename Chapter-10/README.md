# Chapter 10: Using Separate Header and Footer Templates in Django

In this chapter, we'll continue our project by creating separate HTML files for the header and footer sections of our website. We'll then use the `{% include %}` template tag to include these files in multiple pages of our Django project.

## Prerequisites

Before proceeding, ensure you have completed Chapter 9 and have your Django project set up with separate header and footer templates.

## Getting Started

1. **Create Separate Header and Footer Templates:**

    Create separate HTML files for the header and footer sections of your website. For example, create `header.html` and `footer.html` files within your `templates` folder.

2. **Define Header and Footer Content:**

    In the `header.html` and `footer.html` files, define the content that should appear in the header and footer sections of your website, respectively. For example:

    ```html
    <!-- header.html -->
    <header>
        <!-- Header content here -->
    </header>

    <!-- footer.html -->
    <footer>
        <!-- Footer content here -->
    </footer>
    ```

3. **Include Header and Footer in Other Templates:**

    In other templates where you want to include the header and footer, use the `{% include %}` template tag to include the respective HTML files. For example, in your `index.html` and `about.html` files:

    ```html
    <!-- index.html -->
    {% include "header.html" %}

    <!-- Page-specific content here -->

    {% include "footer.html" %}

    <!-- about.html -->
    {% include "header.html" %}

    <!-- Page-specific content here -->

    {% include "footer.html" %}
    ```

    This ensures that the header and footer are included in multiple pages of your Django project, allowing for easier management and consistency across pages.

## Next Steps

Congratulations! You've successfully implemented separate header and footer templates in your Django project and included them in multiple pages using the `{% include %}` template tag. In the next chapter, we'll explore more advanced techniques for enhancing the user experience and optimizing performance in Django.

