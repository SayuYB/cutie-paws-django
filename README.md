CUTIE PAWS – PET ADOPTION & ESSENTIALS STORE

Cutie Paws is a vibrant Django-based web application that serves as both a pet adoption hub and a pet product store. It aims to provide a seamless user experience while promoting animal welfare and responsible pet ownership.

Project Overview

Cutie Paws is your one-stop destination for everything pet-related. From high-quality food and grooming products to personalized pet care recommendations and an intuitive pet adoption system, Cutie Paws is dedicated to pet happiness and customer satisfaction.

Objectives

- Pet Essentials: Provide quality food, toys, grooming products, and accessories.
- Pet Adoption Hub: Connect pet lovers with deserving, adoptable pets.
- Your Pet’s Pick: Offer personalized care suggestions based on pet type and user preferences.
- User Experience: Ensure easy navigation, responsive design, and engaging interactions.

Features

- Pet listings with descriptions and images
- Browse and manage pet care products
- Submit pet adoption requests via forms
- Secure admin panel for managing pets, products, and user data
- Static and media file support

Technologies Used

- Backend: Python, Django
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite / MySQL
- Others: Django Admin

Scope

- Build a dynamic and user-friendly interface for browsing and managing pets and products.
- Provide tailored recommendations to users based on pet profiles.
- Serve as a platform that merges commerce with compassion.

Limitations

- Data privacy and security measures are basic
- Subject to technical and hosting constraints
- Requires trust-building with users
- Operates in a competitive online space
- Must align with pet industry regulations

How to Run Locally

1. Create and activate a virtual environment  
   python -m venv venv  
   source venv/bin/activate   (On Windows: venv\Scripts\activate)

2. Install dependencies  
   pip install mysqlclient  
   pip install Pillow

3. Apply migrations  
   python manage.py makemigrations  
   python manage.py migrate

4. Run the server  
   python manage.py runserver

5. Visit http://127.0.0.1:8000

Database & Admin Panel

Database Configuration

This project uses MySQL as the database. To connect your local MySQL instance with the Django app, update the DATABASES settings in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Note: Replace the placeholders with your own MySQL credentials. Do not commit actual passwords to version control.

Django Admin Panel

This project includes a fully functional Django Admin panel to manage:

- Pet listings
- Product inventory
- Adoption requests
- User submissions

To access it:

1. Create a superuser (if not already done):  
   python manage.py createsuperuser

2. Run the server and visit:  
   http://127.0.0.1:8000/admin

3. Log in with your superuser credentials.

Academic Note

This project was developed as part of an academic course and is intended for educational and demonstration purposes only. It is not a commercial product.
