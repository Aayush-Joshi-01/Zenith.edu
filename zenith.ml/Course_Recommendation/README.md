# Course Recommendation API

This Flask-based API provides course recommendations based on user preferences such as course level and interests. It utilizes Flask-RESTful for building RESTful endpoints and supports CORS for cross-origin requests.

## Requirements

To run this application, ensure you have the following installed:

- Python 3.7+
- Flask
- Flask-RESTful
- Flask-CORS

You can install the required Python packages using pip:

```bash
pip install Flask Flask-RESTful Flask-CORS
```

## Running the Application

To start the Flask server and run the API, execute the following command in your terminal:

```bash
python api_request.py
```

This will start the Flask development server on `http://0.0.0.0:5002`.

## API Endpoints

### POST /recommend

This endpoint accepts a JSON payload with user preferences and returns a list of recommended courses.

#### Request

```json
{
    "user_id": "123",
    "level": "Intermediate",
    "interests": ["Machine Learning", "Web Development"]
}
```

- `user_id`: Identifier for the user (optional).
- `level`: Desired level of the course (`Beginner`, `Intermediate`, `Advanced`, `Any`).
- `interests`: List of interests related to course categories (e.g., `Programming`, `Machine Learning`, `Web Development`).

#### Response

```json
[
    {
        "id": 2,
        "name": "Machine Learning Fundamentals",
        "description": "Introduction to machine learning algorithms and techniques.",
        "level": "Intermediate",
        "category": "Machine Learning"
    },
    {
        "id": 3,
        "name": "Web Development with Flask",
        "description": "Build web applications using Flask framework.",
        "level": "Intermediate",
        "category": "Web Development"
    }
]
```

- `id`: Unique identifier for the course.
- `name`: Name of the course.
- `description`: Description or overview of the course.
- `level`: Difficulty level of the course.
- `category`: Category or field of study related to the course.

If there are no courses matching the criteria, an empty array `[]` will be returned.

## Code Structure

### `api_request.py`

This file contains the main application logic, including setup of Flask app, definition of API endpoints, and course recommendation logic.

### Dummy Course Data

The `courses` list within `api_request.py` provides sample course data for demonstration purposes. In a real-world application, this data would typically be fetched from a database or an external API.

## Logging

The application uses Python's logging module to log information and errors. By default, it logs all information at the `INFO` level. You can configure the logging level and format as needed.

## Notes

- Customize the course data (`courses` list) or integrate with a database to fetch actual course information dynamically.
- Ensure the Flask server (`api_request.py`) is running and accessible to make requests to the API endpoints.

This README provides an overview and basic usage instructions for the Course Recommendation API. Modify and extend the application according to your specific requirements and use cases.
