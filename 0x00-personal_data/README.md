# ALX Backend User Data



## Overview
This project focuses on handling personal data in backend systems, specifically focusing on obfuscation, logging, encryption, and secure database access. By the end of this project, you should be able to:

- Identify and handle Personally Identifiable Information (PII).
- Implement logging mechanisms to obscure sensitive data.
- Securely handle passwords using encryption techniques.
- Safely connect and interact with a database using environment variables for sensitive information.

## Project Tasks

### Task 0: Regex-ing
Write a function called `filter_datum` that returns an obfuscated log message using regex.

### Task 1: Log Formatter
Update the `RedactingFormatter` class to format log records and obfuscate sensitive fields.

### Task 2: Create Logger
Implement a `get_logger` function to create a logger that uses `RedactingFormatter` for sensitive data fields.

### Task 3: Connect to Secure Database
Implement a `get_db` function to securely connect to a database using credentials stored in environment variables.

### Task 4: Read and Filter Data
Create a `main` function to retrieve and log user data from the database, obfuscating sensitive fields.

### Task 5: Encrypting Passwords
Implement a `hash_password` function to hash passwords using bcrypt.

### Task 6: Check Valid Password
Implement an `is_valid` function to verify passwords against their hashed versions.

## Resources
- [What Is PII, non-PII, and Personal Data?](https://link-to-resource)
- [logging documentation](https://docs.python.org/3/library/logging.html)
- [bcrypt package](https://pypi.org/project/bcrypt/)
- [Logging to Files, Setting Levels, and Formatting](https://realpython.com/python-logging/)

## Requirements
- Python 3.7 on Ubuntu 18.04 LTS
- Use `#!/usr/bin/env python3` as the first line of all your Python files
- All files should end with a new line
- A `README.md` file at the root of the project directory
- Use `pycodestyle` for code style (version 2.5)
- All modules, classes, and functions must have proper documentation
- All functions should be type annotated
