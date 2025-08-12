# project structure alx_travel_app
The alxtravelapp project is a real-world Django application that serves as the foundation for a travel listing platform. This milestone focuses on setting up the initial project structure, configuring a robust database, and integrating tools to ensure API documentation and maintainable configurations.

---

## 📦 Milestone 1 Project Reflection Summary:
Building a professional-grade Django REST API-based travel listing platform called alxtravelapp, with strong foundations in:

Scalable structure (project + app).
Clean dependency management.
Secure environment handling.
Robust API docs (Swagger).
Future-ready background tasks (Celery + RabbitMQ).
Git-based version control and public repository management.

These practices align very well with real-world backend engineering standards and will make the app easy to scale and maintain.


# 🚀 Features
🔍 View and manage property listings
🗕️ Create and track bookings
⭐ Leave and read reviews for listings
🔐 Integrated with Django’s built-in User model
🛠 Powered by Django REST Framework
🧪 Seeder to populate sample data
 

# 🧱 Tech Stack
Python 3
django 5.2
djangorestframework
django-cors-headers
drf-yasg
django-environ
celery, rabbitmq (for future use)
Freeze requirements into requirements.tx
Seeding


# Project structure

alx_travel_app/
├── alx_travel_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── listings/
│   ├── __init__.py
│   ├── views.py
│   ├── models.py
│   └── ...
├── manage.py
├── requirements.txt
└── venv/

---

## 📦 Milestone 2 Create Database Modeling and Data Seeding – alx_travel_app_0x00

This task sets up the **core data models**, **API serializers**, and a **database seeder** for the `alx_travel_app_0x00` Django project. It is a foundational step in building a travel listing platform with sample data for development and testing.


## ✅ Objectives

1. Duplicate the project structure.
2. Define the database models: `Listing`, `Booking`, `Review`.
3. Create serializers for `Listing` and `Booking`.
4. Implement a management command to seed the database.
5. Populate the database with sample data using the seeder.

---

## 🚀 Milestone 3: Creating Views and API Endpoints

Base URL: `/api/`

| Endpoint              | Method | Description              |
|-----------------------|--------|--------------------------|
| /listings/            | GET    | List all listings        |
| /listings/            | POST   | Create new listing       |
| /listings/{id}/       | GET    | Get listing by ID        |
| /listings/{id}/       | PUT    | Update listing by ID     |
| /listings/{id}/       | DELETE | Delete listing by ID     |
| /bookings/            | GET    | List all bookings        |
| /bookings/            | POST   | Create new booking       |
| /bookings/{id}/       | GET    | Get booking by ID        |
| /bookings/{id}/       | PUT    | Update booking by ID     |
| /bookings/{id}/       | DELETE | Delete booking by ID     |

📘 Swagger Docs available at: `/swagger/`
