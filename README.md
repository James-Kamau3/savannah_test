# Customer Orders API Service
## Overview
This project is a Customer Orders API Service built with Python Django. It provides a RESTful API for managing customers and their orders. The service implements secure authentication and authorization using OpenID Connect and sends SMS alerts to customers via the Africa's Talking SMS Gateway whenever an order is added. The application is equipped with unit tests, CI/CD pipelines, to be deployed IaaS platform.


### Features

### Customer Management
Add, view, update, and delete customers.
Each customer includes a name and a unique code.

### Order Management
Add and list orders linked to specific customers.
Orders include item details, amount, and timestamp.

### Authentication and Authorization
Implemented using OpenID Connect to ensure secure access.

### SMS Notifications
Sends SMS alerts to customers when a new order is created using the Africa's Talking SMS Gateway.

### Unit Testing
Comprehensive test coverage with Django's testing framework.

### CI/CD
Automated continuous integration and deployment pipelines.


## Installation and Setup
### Prerequisites
Python 3.8 or higher
Django 5.1.3
A registered Africa's Talking developer account (sandbox or production)
OpenID Connect provider details
Docker (for containerized deployment)

## Steps
1. Clone the Repository
`git clone https://github.com/James-Kamau3/savannah_test`

2. Set Up a Virtual Environment
`python3 -m venv venv`
`source venv/bin/activate`

3. Install Dependencies
`pip install -r requirements.txt`


5. Run Database Migrations
`python manage.py migrate`

6. Start the Development Server
`python manage.py runserver`