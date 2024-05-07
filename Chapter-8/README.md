# Chapter 8: Passing Data in Loops and Conditional Statements from View to Template

In this chapter, we'll pass data in loops and conditional statements from a Django view to a template. This allows us to iterate over lists, apply conditions, and render dynamic content in our HTML pages based on the provided data.

## Prerequisites

Before proceeding, ensure you have completed Chapter 7 and have your Django project set up with passing data from view to template in loops and conditional statements.

## Getting Started

1. **Update View Function:**

    In your `views.py` file, update the view function to include data to be looped through and evaluated with conditional statements in the template. For example:

    ```python
    def homepage(request):
        data = {
            'title': 'Home Page',
            'header': 'Welcome to my Page',
            'course_list': ['Python', 'Java', 'C Sharp'],
            'student_details': [
                {'Name': 'Hamza', 'Phone': '0333123456'},
                {'Name': 'Ahmed', 'Phone': '0315123456'}
            ],
            'Numbers': [10, 20, 30, 40, 50, 60, 70]
        }
        return render(request, "index.html", data)
    ```

    In this example, we've added a list named `Numbers` to the `data` dictionary, containing integer values for evaluation with conditional statements in the template.

2. **Update HTML Template:**

    In your `index.html` file within the `templates` folder, update the HTML structure to loop through the data and apply conditional statements based on the provided data. For example:

    ```html
    {% if Numbers|length > 0 %}
        {% for num in Numbers %}
            {% if num > 20 and num < 70 %}
                <div>{{ num }}</div>
            {% endif %}
        {% endfor %}
    {% else %}
        No Data Found
    {% endif %}
    ```

    In this example, we use `{% if %}` and `{% endif %}` template tags to apply a conditional statement based on the length of the `Numbers` list. Within the loop, we use another `{% if %}` statement to check if each number is within a specific range before rendering it in the HTML page.

## Next Steps

Congratulations! You've successfully passed data in loops and conditional statements from a Django view to a template and rendered dynamic content based on the provided data. In the next chapter, we'll explore What is CSS, JavaScript & Images in Django and How to use them.

