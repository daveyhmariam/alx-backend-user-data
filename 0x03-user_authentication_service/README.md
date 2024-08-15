# User Authentication Service

This project implements a user authentication service using Python's Flask framework. For learning purposes, this project walks through every step of building an authentication system.

## Curriculum
- Short Specializations
- **Average**: 39.77%

## Project Information
**Back-end**: Flask, SQLAlchemy  
**Weight**: 1  
**Project Timeline**:  
- Start: Aug 12, 2024, 6:00 AM  
- End: Aug 16, 2024, 6:00 AM  
- Checker released: Aug 13, 2024, 6:00 AM  

## Learning Objectives

By the end of this project, you should be able to:
- Declare API routes in a Flask app.
- Get and set cookies.
- Retrieve form data from requests.
- Return various HTTP status codes.
- Implement authentication mechanisms.

## Setup

Install `bcrypt` using:

```bash
pip3 install bcrypt

Tasks Overview
0. User Model
Create a SQLAlchemy model named User for the users table.
1. Create User
Implement the add_user method in the DB class.
2. Find User
Implement DB.find_user_by method to retrieve users by attributes.
3. Update User
Implement DB.update_user to update user details.
4. Hash Password
Create a _hash_password method to securely hash passwords using bcrypt.
5. Register User
Implement Auth.register_user to create new users and store hashed passwords.
6. Basic Flask App
Create a basic Flask app with a single route GET / returning JSON.
7. Register User Endpoint
Implement the POST /users endpoint to register users.
8. Credentials Validation
Implement Auth.valid_login to validate login credentials.
9. Generate UUIDs
Implement a private _generate_uuid function for creating session IDs.
10. Get Session ID
Implement Auth.create_session to create a session for a user.
11. Login
Implement the POST /sessions route to log in users.
12. Find User by Session ID
Implement Auth.get_user_from_session_id to retrieve users based on session ID.
13. Destroy Session
Implement Auth.destroy_session to clear a user’s session.
14. Logout
Implement the DELETE /sessions route to log out users.
