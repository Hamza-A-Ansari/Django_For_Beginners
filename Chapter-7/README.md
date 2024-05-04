# Chapter 7: Passing Data in a Loop from View to Template

In this chapter, we'll pass data in a loop from a Django view to a template. This allows us to iterate over lists or dictionaries of data and render it dynamically in our HTML pages using loops.

## Prerequisites

Before proceeding, ensure you have completed Chapter 6 and have your Django project set up with passing data from view to template configured.

## Getting Started

1. **Update View Function:**

    In your `views.py` file, update the view function to include data to be looped through in the template. For example:

    ```python
    def homepage(request):
        data = {
            'title': 'Home Page',
            'header': 'Welcome to my Page',
            'course_list': ['Python', 'Java', 'C Sharp'],
            'student_details': [
                {'Name': 'Hamza', 'Phone': '0333123456'},
                {'Name': 'Ahmed', 'Phone': '0315123456'}
            ]
        }
        return render(request, "index.html", data)
    ```

    In this example, we've added two lists (`course_list` and `student_details`) to the `data` dictionary. These lists contain data to be looped through in the template.

2. **Update HTML Template:**

    In your `index.html` file within the `templates` folder, update the HTML structure to loop through the data passed from the view. For example:

    ```html
    <html>
        <head>
            <title>{{ title }}</title>
        </head>
        <body>
            <h1>{{ header }}</h1>

            {% for course in course_list %}
            <div>{{ forloop.counter }} {{ course }}</div>
            {% endfor %}

            <br/>
            <table border="1" cellpadding="10">
                <tr>
                    <th>Name</th>
                    <th>Phone Number</th>
                </tr>

                {% for student in student_details %}
                <tr>
                    <td>{{ student.Name }}</td>
                    <td>{{ student.Phone }}</td>
                </tr>
                {% endfor %}

            </table>
        </body>
    </html>
    ```

    In this example, we use `{% for %}` and `{% endfor %}` template tags to loop through the `course_list` and `student_details` data passed from the view. Within the loop, we access individual items using dot notation (`{{ course }}`, `{{ student.Name }}`, `{{ student.Phone }}`).

## Next Steps

Congratulations! You've successfully passed data in a loop from a Django view to a template and rendered dynamic content in your HTML page. In the next chapter, we'll explore If Else statement Django template.

