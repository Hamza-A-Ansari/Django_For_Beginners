# Chapter 2: Setting Up Database with Migrations

In this chapter, we'll continue setting up our Django project by configuring the database using migrations. Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

## Prerequisites

Before proceeding, ensure you have completed Chapter 1 and have your Django project set up.

## Getting Started

1. **Create Initial Migrations:**

    Django comes with a set of built-in migrations that define the initial state of the project's apps. To apply these migrations to your database, use the following command:

    ```bash
    python manage.py migrate
    ```

    This command will create database tables for all installed applications and apply any initial data migrations.

    **Note:** If you've made changes to your models, Django will create new migrations to reflect those changes. You'll need to run `python manage.py makemigrations` to generate the migration files and then run `python manage.py migrate` to apply them.

2. **Create Superuser:**

    To access the Django admin portal and perform administrative tasks, you need to create a superuser account. Run the following command and follow the prompts to set up the superuser:

    ```bash
    python manage.py createsuperuser
    ```

    This command will prompt you to enter a username, email address, and password for the superuser account.

## Next Steps

Congratulations! You've successfully set up your database using migrations and created a superuser for accessing the Django admin portal. In the next chapter, we'll start building our Django application by creating models and defining their relationships.

