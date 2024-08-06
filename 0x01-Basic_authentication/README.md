# Basic Authentication

## Description
In this project, you will learn what the authentication process means and implement Basic Authentication on a simple API. This project is for learning purposes and will walk through each step of the mechanism to understand it by doing.




## Setup and Start Server
```bash
pip3 install -r requirements.txt
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app


Tasks
0. Simple-basic-API
Download and start the project from archive.zip.
Start the server and test the status endpoint.
1. Error handler: Unauthorized
Add an error handler for status code 401 in api/v1/app.py.
Add a new endpoint in api/v1/views/index.py that raises a 401 error.
2. Error handler: Forbidden
Add an error handler for status code 403 in api/v1/app.py.
Add a new endpoint in api/v1/views/index.py that raises a 403 error.
3. Auth class
Create a class Auth in api/v1/auth/auth.py with methods require_auth, authorization_header, and current_user.
4. Define which routes don't need authentication
Update require_auth method to check excluded paths.
5. Request validation
Update authorization_header method to return the value of the Authorization header if present.
Implement before_request method in api/v1/app.py to handle request validation.
6. Basic auth
Create a class BasicAuth that inherits from Auth.
7. Basic - Base64 part
Add extract_base64_authorization_header method in BasicAuth.
8. Basic - Base64 decode
Add decode_base64_authorization_header method in BasicAuth.
9. Basic - User credentials
Add extract_user_credentials method in BasicAuth.
10. Basic - User object
Add user_object_from_credentials method in BasicAuth.
11. Basic - Overload current_user - and BOOM!
Overload current_user method in BasicAuth.
