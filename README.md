# FastAPI Clean Architecture Project

This project is a RESTful API built with FastAPI, following clean architecture principles. It provides a solid foundation for building scalable and maintainable web applications.

## Project Structure

```
project_name/
├── pyproject.toml
├── .env
├── .gitignore
├── README.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   └── services/
└── tests/
```

- `src/`: Contains all the source code.
  - `config/`: Configuration management.
  - `api/`: HTTP-related concerns (routes, dependencies).
  - `core/`: Core functionality (e.g., security).
  - `db/`: Database-related code.
  - `models/`: Domain models representing business entities.
  - `repositories/`: Data access layer.
  - `schemas/`: Pydantic models for request/response schemas.
  - `services/`: Business logic layer.
- `tests/`: Contains all tests.

## Libraries Used

This project uses several key libraries:

1. **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.

2. **Uvicorn**: An ASGI web server implementation for Python.

3. **Pydantic**: Data validation and settings management using Python type annotations.

4. **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library.

5. **Python-dotenv**: Reads key-value pairs from a .env file and sets them as environment variables.

6. **Pytest**: Testing framework.

7. **Black**: Code formatter.

8. **isort**: Import sorter.

9. **Flake8**: Style guide enforcer.

## Setup and Installation

1. Ensure you have Python 3.9+ and Poetry installed on your system.

2. Clone the repository:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

3. Install dependencies:
   ```
   poetry install
   ```

4. Set up your `.env` file with necessary environment variables (e.g., `DATABASE_URL`).

5. Run the application:
   ```
   poetry run uvicorn src.main:app --reload
   ```

## Running Tests

To run tests, use the following command:

```
poetry run pytest
```

## Code Formatting and Linting

- To format code using Black:
  ```
  poetry run black .
  ```

- To sort imports using isort:
  ```
  poetry run isort .
  ```

- To run Flake8 for style guide enforcement:
  ```
  poetry run flake8
  ```

## Contributing

Please read our contributing guidelines before submitting pull requests.

## License

[Specify your license here]