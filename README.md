# HRMS(Human Resource Management System)
## The Basic HRMS (Human Resource Management System) is a web-based application designed to manage employee records, track attendance, and generate basic reports within an organization. It provides a simple and effective way to manage human resources by offering functionalities such as:

- *Employee Management*: Store and manage employee information like names, designations, departments, and joining dates.
### Technologies used
- *Programming Language*: Python
- *Framework*: Django
- *Database*: SQLite (default), but can be replaced with MySQL.
- *Frontend*: HTML
- *API*: Django REST Framework
  
# To run the Basic HRMS project
### 1. Clone the Repository
First, clone the repository to local machine
### 2. Set Up a Virtual Environment (Optional but Recommended)
Creating a virtual environment helps manage dependencies specific to this project:
- python -m virtualenv name_of_virtualenvironment
- cd name_of_virtualenvironment
- cd scripts
- activate
### 3. Install Dependencies
Install the required Python packages and djangorestframework
### 4. Set Up the Database
Django requires setting up the database schema before running the application. Run these commands:
- python manage.py migrate
- python manage.py makemigrations
- python manage.py migrate
### 5. Run the Development Server
Start the Django development server using:
- python manage.py runserver

By default, the application will be accessible at http://127.0.0.1:8000/ in web browser.
### 6. Access the Application
Open web browser and navigate to:
http://127.0.0.1:8000/sufix
### 7.Stop the Server
To stop the server,use ctrl+c in the terminal where the server is running.
### 8.Deactivate the virtual Environment
using deactivate
