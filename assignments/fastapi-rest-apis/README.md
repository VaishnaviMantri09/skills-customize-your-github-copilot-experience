# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using the FastAPI framework, including defining endpoints, validating request data with Pydantic, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create a Book Library API

#### Description
Build a FastAPI application that manages a simple library of books. Implement endpoints to list books, get book details, add new books, update books, and delete books.

#### Requirements
Completed program should:

- Define a FastAPI application in `starter-code.py`.
- Implement the following routes:
  - `GET /books` to return a list of books.
  - `GET /books/{book_id}` to return a single book by ID.
  - `POST /books` to add a new book.
  - `PUT /books/{book_id}` to update an existing book.
  - `DELETE /books/{book_id}` to remove a book.
- Use Pydantic models to validate request data.
- Return JSON responses with appropriate HTTP status codes.
- Include example `curl` or HTTP requests in comments.

### 🛠️ Add Validation and Error Handling

#### Description
Extend the API to validate incoming data and handle common error cases such as missing books or invalid input.

#### Requirements
Completed program should:

- Validate that each book includes `title`, `author`, and `year` fields.
- Ensure `year` is a positive integer.
- Return a 404 error if a requested book ID does not exist.
- Return a 400 error if the request body is invalid.
- Provide clear error messages in JSON format.
