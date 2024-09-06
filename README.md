# BlogProject

## Overview

BlogProject is a blogging platform designed to enable users to interact with blog content and manage their posts. The project includes user authentication features and a straightforward blog interface for managing and viewing posts. It now also offers the ability to generate post descriptions using ChatGPT.

## Features

- **Login Page**: Allows users to log in to their accounts to access restricted features.
- **Registration Page**: Enables new users to create an account on the platform.
- **Home Page**: Displays recent blog posts and provides navigation to other pages.
- **Contact Us Page**: Provides a form for users to contact the site administrators.
- **Create Posts Page**: Allows authenticated users to create new blog posts.
    - **Manual Post Creation**: Users can manually create blog posts by entering the title and description.
    - **AI-Assisted Post Creation (via ChatGPT)**: Users can generate post descriptions automatically by providing a title, and ChatGPT will create the content for the description.
- **Comments**: Logged-in users can comment on blog posts.
Manual Post Creation
AI-Assisted Post Creation (via ChatGPT)
## Access Control

The following features are only available to logged-in users:

- **Commenting on Posts**: Users must be logged in to add comments to posts.
- **Contact Us**: The contact form is accessible only to logged-in users.
- **Creating Posts**: Only logged-in users can create new posts.
- **Manual Post Creation**: Logged-in users can manually write both titles and descriptions for their blog posts.
- **AI-Assisted Post Creation**: Users can use ChatGPT to automatically generate the post description by providing only the title.

Users who are not logged in will have access only to the home page and will not be able to use the commenting, contact, post creation, or ChatGPT description features.

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/BlogProject.git
    cd BlogProject
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser (admin):
    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

8. Access the application:

    Open `http://127.0.0.1:8000/` in your browser.

## Contributing

Contributions are welcome. Please:

1. Fork the repository.
2. Create a new branch.
3. Make changes.
4. Commit changes.
5. Push to your fork.
6. Create a pull request.

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
