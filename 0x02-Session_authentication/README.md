# Session Authentication - README

## Background Context
In this project, you will implement a Session Authentication system from scratch. While in the industry, using pre-built modules like `Flask-HTTPAuth` for authentication is standard practice, this project focuses on understanding the core concepts by building it step by step.

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without the help of Google:
- What authentication means.
- What session authentication means.
- What Cookies are and how to send and parse them.

## Requirements
- All scripts must be written in Python 3.7 and will be executed on Ubuntu 18.04 LTS.
- The first line of all your Python files should be `#!/usr/bin/env python3`.
- A `README.md` file at the root of the folder is mandatory.
- Your code should follow the `pycodestyle` style (version 2.5).
- All modules, classes, and functions must have proper documentation.

## Resources
Read or watch:
- REST API Authentication Mechanisms (focus on session auth)
- HTTP Cookie
- Flask
- Flask Cookie

## Project Structure

### Tasks

#### 0. **Et moi et moi et moi!**
- **Task:** Implement a new endpoint `GET /users/me` to retrieve the authenticated User object.
- **Requirements:** 
  - Copy all your work from the previous project `0x06. Basic authentication`.
  - Implement the new endpoint in the file `api/v1/views/users.py`.

#### 1. **Empty session**
- **Task:** Create a `SessionAuth` class that inherits from `Auth`. 
- **Requirements:** 
  - The class should be empty and is a base for further implementation.

#### 2. **Create a session**
- **Task:** Update the `SessionAuth` class to manage session creation.
- **Requirements:** 
  - Create an in-memory dictionary `user_id_by_session_id` to store session IDs.
  - Implement the method `create_session(self, user_id: str) -> str` to generate a new session ID for a user ID.

#### 3. **User ID for Session ID**
- **Task:** Implement a method to retrieve a User ID from a Session ID.
- **Requirements:**
  - Implement `user_id_for_session_id(self, session_id: str) -> str` to return the User ID associated with a session ID.

#### 4. **Session cookie**
- **Task:** Implement session cookie handling in the `Auth` class.
- **Requirements:** 
  - Implement `session_cookie(self, request=None)` to retrieve the session ID from cookies.

#### 5. **Before request**
- **Task:** Update the `@app.before_request` method to handle session authentication.
- **Requirements:** 
  - Ensure requests are blocked if both `authorization_header` and `session_cookie` are `None`.

### Additional Information
- The session ID should be managed via cookies using the name defined by the environment variable `SESSION_NAME`.
- To switch authentication methods, use the `AUTH_TYPE` environment variable (e.g., `session_auth`, `basic_auth`).

## Getting Started

1. Clone the repository and navigate to the project directory.
2. Set up your environment variables for `AUTH_TYPE` and `SESSION_NAME`.
3. Start the Flask server and test the endpoints using tools like `curl` or Postman.

```bash
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
