Django Project: Basic Configuration
This Django project provides a basic configuration for starting a website with two related templates and an administration interface.

Installation
Clone this repository on your local machine:
`git clone <url-repository`.

Install the project dependencies:
`pip install -r requirements.txt`

Configuration
Make sure you have Django installed. If you don't have it, you can install it using pip:
`pip install Django`

Apply migrations to create the initial database:
`python manage.py migrate`.

To run the development server, use the following command:
`python manage.py runserver`

Models
This project contains two related models:

Model One: Author
Model Two: Books

Administration Interface
You can access the administration interface to manage the created models. To do so, follow these steps:

Run the development server.
Open your web browser and visit http://localhost:8000/admin/.
Log in with the superuser credentials you created during the initial setup.Once logged in, you will be able to view and manage the models from the administration interface.

Contributions
If you wish to contribute to this project, you are welcome to do so! Feel free to open an issue or send a pull request with your suggestions or changes.

Acknowledgements
This project is based on the Django framework and has been created with the purpose of providing a basic setup to start developing web applications using Django.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
