E-commerce Store with Django
This is an e-commerce store built with Django, a Python web framework. The store has a user interface that allows users to browse products, add items to their cart, and checkout.

Getting Started
Prerequisites
You need to have the following software installed on your computer to get started:

Python (version 3.6 or higher)
pip (version 20.0 or higher)
MySQL (version 5.7 or higher)
Installation
To get started, clone the repository to your local machine:

bash
Copy code
git clone https://github.com/Eniiyanu/Eccomerce-Store.git
Then, navigate to the project directory:

bash
Copy code
cd Eccomerce-Store
Next, create a virtual environment and activate it:

bash
Copy code
python3 -m venv env
source env/bin/activate
Install the project dependencies:

bash
Copy code
pip install -r requirements.txt
Create a MySQL database for the project and update the DATABASES setting in settings.py to reflect your database settings.

Run the database migrations:

bash
Copy code
python manage.py migrate
Create a superuser for the admin site:

bash
Copy code
python manage.py createsuperuser
Start the development server:

bash
Copy code
python manage.py runserver
Usage
Visit http://localhost:8000/ to access the home page of the e-commerce store. From there, users can browse products, add items to their cart, and checkout.

To access the admin site, visit http://localhost:8000/admin/ and log in with the superuser account you created earlier. From the admin site, you can manage products, orders, and other aspects of the store.




