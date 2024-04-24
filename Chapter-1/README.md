# Chapter 1: Setting Up Your Django Project

In this chapter, we'll walk through the initial setup of your Django project. We'll start by creating a new project using the `django-admin` command and then run the development server to ensure everything is working as expected.

## Prerequisites

Before getting started, ensure you have the following installed on your system:

- Python (version 3.x recommended)
- Django framework

## Getting Started

1. **Create a New Django Project:**

    Use the following command to create a new Django project:

    ```bash
    django-admin startproject <project_name>
    ```

    Replace `<project_name>` with the desired name for your project.

2. **Run the Development Server:**

    Navigate into the project directory:

    ```bash
    cd <project_name>
    ```

    Then, start the development server using the following command:

    ```bash
    python manage.py runserver
    ```

    This will start the development server on your local machine, and you should see output similar to the following:

    ```plaintext
    Django version <version>, using settings 'project_name.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```

    Your Django project is now running locally at `http://127.0.0.1:8000/`. Open this URL in your web browser to view the default Django welcome page.

## Next Steps

Congratulations! You've successfully set up your Django project and run the development server. In the next chapter, we'll dive deeper into Django's project structure and start building our application.

