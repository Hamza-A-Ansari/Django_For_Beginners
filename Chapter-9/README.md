# Chapter 9: Using Static Files (CSS, Images, JavaScript) in Django

In this chapter, we'll explore how to use static files such as CSS, images, and JavaScript in a Django project. Static files are assets that are served directly to the client without any processing by the server.

## Prerequisites

Before proceeding, ensure you have completed Chapter 8 and have your Django project set up with passing data in loops and conditional statements from a Django view to a template.

## Getting Started

1. **Create Static Folder:**

    Create a `static` folder in the same directory where your `templates` folder lies. This folder will contain your static files such as CSS, images, and JavaScript.

2. **Organize Static Files:**

    Within the `static` folder, organize your static files into subfolders according to their types. For example, create `css`, `images`, and `javascript` folders for CSS files, image files, and JavaScript files, respectively.

3. **Add Static Files:**

    Place your CSS files in the `css` folder, image files in the `images` folder, and JavaScript files in the `javascript` folder. Ensure that the filenames and file paths are appropriately structured.

4. **Configure Settings:**

    Open your `settings.py` file located in your project directory. Add the following code snippet to the end of the file to specify the location of your static files:

    ```python
    STATICFILES_DIRS = [
        BASE_DIR, "static"
    ]
    ```

    This code tells Django to look for static files in the `static` folder within your project directory.

5. **Link Static Files in HTML Template:**

    In your HTML template (e.g., `index.html`), link to your static files using the appropriate HTML tags. For example, to link CSS files, use the `<link>` tag, and for images, use the `<img>` tag. Ensure that you specify the correct paths to your static files relative to the `static` folder. For example:

    ```html
    <link rel="stylesheet" href="static/css/h_style.css">
    <div class="header">
        <!-- Header content here -->
    </div>

    <link rel="stylesheet" href="static/css/im_style.css">
    <div class="center">
        <img src="static/images/image.jpg" alt="Sample Image">
    </div>
    ```

    In this example, we've linked CSS files (`h_style.css` and `im_style.css`) located in the `css` folder within the `static` folder. We've also included an image (`image.jpg`) located in the `images` folder within the `static` folder.

## Next Steps

Congratulations! You've successfully used static files such as CSS, images, and JavaScript in your Django project. In the next chapter, we'll explore more advanced techniques for enhancing the user experience and optimizing performance in Django.

