# Library-Management-API
(a) How to Run the Project

Prerequisites

To run this project, ensure you have the following installed on your system:

Python 3.8+

pip (Python package installer)

Flask

Steps to Run the Project

Clone the Repository:

git clone <repository_url>
cd <repository_folder>

Install Dependencies:
Install the required Python packages using pip:

pip install flask

Run the Flask Application:
Start the development server by running:

python <filename>.py

Replace <filename> with the name of the Python file containing the Flask code.

Access the API:
Open your browser or a tool like Postman, and access the API at:

http://127.0.0.1:5000

Endpoints Available

Books

GET /books - Fetch all books (supports search, pagination).

POST /books - Create a new book.

GET /books/<int:book_id> - Fetch a specific book by ID.

PUT /books/<int:book_id> - Update a book by ID.

DELETE /books/<int:book_id> - Delete a book by ID.

Members

GET /members - Fetch all members.

POST /members - Create a new member.

GET /members/<int:member_id> - Fetch a specific member by ID.

PUT /members/<int:member_id> - Update a member by ID.

DELETE /members/<int:member_id> - Delete a member by ID.

Authentication

All endpoints require a valid token in the Authorization header in the format:

Bearer your_secure_token

(b) Design Choices Made

1. Token-based Authentication

A simple token-based authentication system was implemented to secure API endpoints.

2. Separation of Concerns

Utility functions (locate_book and locate_member) handle data retrieval, ensuring clean and reusable code.

3. CRUD Structure

Each resource (Books and Members) has its own set of CRUD operations, providing clear and predictable API behavior.

4. Pagination for Books

Pagination and search functionality were added to the GET /books endpoint to improve performance and usability when dealing with large datasets.

5. Use of Flask Decorators

The @token_required decorator encapsulates authentication logic, keeping endpoint code clean and focused on business logic.

(c) Assumptions and Limitations

Assumptions

Unique IDs:

Each book and member has a unique id to simplify data management.

In-memory Storage:

Data is stored in memory using Python lists (book_records and member_records).

Valid Token:

A single token (your_secure_token) is used for all authenticated requests.

Basic Search Functionality:

Search on the GET /books endpoint is case-insensitive and matches against the book's title or author.

Limitations

In-memory Storage:

Data will be lost when the server restarts. For production use, a database (e.g., SQLite, PostgreSQL) is recommended.

Token Management:

The token is hardcoded and lacks mechanisms for expiration or rotation.

Concurrency:

The current implementation may encounter issues with concurrent requests due to the lack of thread-safe mechanisms for in-memory storage.

Validation:

Minimal validation is performed on input data; additional validation mechanisms could improve data integrity.

Scalability:

This implementation is best suited for small-scale applications. For larger systems, consider adopting Flask extensions or frameworks like Flask-RESTful or Flask-SQLAlchemy.

Future Improvements

Integrate a database for persistent storage.

Implement user roles and permissions.

Add more robust error handling and logging.

Enhance token-based authentication by using tools like Flask-JWT-Extended.

Add unit tests to ensure code reliability and maintainability.

