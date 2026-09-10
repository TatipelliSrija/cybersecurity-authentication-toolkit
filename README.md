# 🔐 Cybersecurity Authentication Toolkit

## Project Overview

The Cybersecurity Authentication Toolkit is a Flask-based web application that demonstrates secure authentication concepts.

The project implements user registration, password validation, password strength checking, secure password hashing, authentication, and session management.

## Problem Statement

Weak authentication systems can expose applications to unauthorized access and password-related security risks.

This project demonstrates basic security controls that can be used to build a safer authentication system.

## Objective

The objective of this project is to demonstrate:

- User registration
- Password validation
- Password strength checking
- Secure password hashing
- User authentication
- Session management
- Basic security controls

## Features

### 1. User Registration
Users can create an account with a username and password.

### 2. Password Strength Validation
Passwords must contain:

- At least 8 characters
- One uppercase letter
- One lowercase letter
- One number
- One special character

### 3. Secure Password Hashing
Passwords are hashed using Werkzeug's password hashing functionality before being stored in the database.

Plain-text passwords are not stored.

### 4. User Authentication
Users can log in using their registered username and password.

### 5. Session Management
Authenticated users receive a session and can access the protected security dashboard.

### 6. Protected Dashboard
Unauthenticated users cannot directly access the dashboard.

### 7. Logout
Users can securely log out and their session is cleared.

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- Werkzeug Security

## Project Structure

```text
cybersecurity-authentication-toolkit/
│
├── templates/
│   ├── register.html
│   ├── login.html
│   └── dashboard.html
│
├── static/
│
├── app.py
├── database.py
├── requirements.txt
├── .gitignore
└── README.md