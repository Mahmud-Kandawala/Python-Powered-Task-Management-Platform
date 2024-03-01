# Python-Powered Task Management Platform

## Objective 

This project encompasses the development of a sophisticated web-based task management application, leveraging Python's Flask framework. It features a meticulously organized directory structure to ensure optimal project scalability and maintainability. The application implements dynamic routing and view rendering to accommodate various functionalities, from user authentication to note management. Utilizing Jinja, a powerful templating engine, alongside HTML, the platform offers an intuitive user interface for tasks such as login, sign-up, and notes manipulation. It supports comprehensive HTTP request handling, including GET and POST methods, to interact with user inputs and server responses effectively.

The backend infrastructure is built upon Flask SQLAlchemy, facilitating seamless database interactions, including model definition, relationship mapping, and CRUD operations. This foundation supports critical features like user account creation, authentication, and session management, ensuring a secure and personalized user experience. Additionally, the application allows for the efficient management of user notes, including adding and deleting notes, demonstrating a practical implementation of database operations in a real-world scenario.


## Methodical Data Flow Overview

1. Template Structure and Inheritance: The application employs Jinja2 for template inheritance in `base.html`, ensuring a consistent look across pages. This methodology streamlines the development process, allowing for modular design and easy updates to the UI/UX.

2. Secure User Authentication: Through `login.html` and `sign_up.html`, user credentials are processed using Flask-WTF, capturing input securely. `auth.py` utilizes Werkzeug for robust password hashing, safeguarding user data during registration and login processes.

3. Personalized User Experience: `home.html` showcases dynamic content rendering, tailored to the logged-in user by fetching data via SQLAlchemy queries in `main.py`. Flask-Login's session management facilitates this personalized interaction, ensuring data is relevant and secure.

4. Interactive Features without Page Reloads: `index.js` integrates AJAX for asynchronous data handling, allowing users to interact with the application—such as adding or deleting notes—without reloading home.html, enhancing the user experience through real-time feedback.

5. Comprehensive Security Measures: The application architecture incorporates Flask-Login for session management and route protection, alongside Flask-WTF for secure form handling, establishing a secure environment for user interactions and data transactions.


## What I Learned

- Advanced Project Structuring: Gained expertise in organizing a project's directory structure to enhance readability, scalability, and maintenance.
- Dynamic Web Routing and Views: Learned to create and manage routes/views in Flask, enabling the development of a multi-page web application with seamless user navigation.
- Jinja Templating and HTML Integration: Mastered the use of Jinja templating language to dynamically render HTML templates, facilitating the creation of a responsive and interactive user interface.
- User Authentication System: Developed a comprehensive understanding of implementing a secure login and sign-up system, including form handling and session management.
- HTTP Protocol Handling: Acquired skills in managing HTTP requests (POST, GET) to effectively process user inputs and server responses.
- Flask SQLAlchemy Database Management: Learned to set up and utilize Flask SQLAlchemy for database interactions, including model creation, foreign key relationships, and database operations.
- Security and Data Integrity: Enhanced knowledge in handling user authentication, session management, and protecting user data against unauthorized access.
- Note Management Features: Implemented functionalities for adding and deleting user notes, applying CRUD operations in a practical scenario and managing user-generated content efficiently.


## Pictures

### Login Screen:
<img src = "images/home.png"> 

### Sign Up Screen:
<img src = "images/signup.png"> 

### Task Add/Removal Screen:
<img src = "images/task.png"> 


## Setup 

Ensure your system is updated with the most recent version of Python.

## Requirments (Install)
```
pip install flask
pip install Flask-SQLAlchemy
pip install flask-login
```

## Viewing The Website

Go to `http://127.0.0.1:5000`
