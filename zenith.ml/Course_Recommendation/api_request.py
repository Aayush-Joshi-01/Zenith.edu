from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import logging

app = Flask(__name__)
api = Api(app)
CORS(app)

# Dummy course data (replace with actual data fetching logic)
courses = [
    {
        "id": 1,
        "name": "Introduction to Python Programming",
        "description": "Learn the basics of Python programming language.",
        "level": "Beginner",
        "category": "Programming"
    },
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
    },
    {
        "id": 4,
        "name": "Advanced Data Analysis with Python",
        "description": "Advanced techniques for data analysis using Python.",
        "level": "Advanced",
        "category": "Data Science"
    }
]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CourseRecommendation(Resource):
    """
    request
    POST /recommend
    Content-Type: application/json

    {
        "user_id": "123",
        "level": "Intermediate",
        "interests": ["Machine Learning", "Web Development"]
    }

    response
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
    """
    def post(self):
        try:
            data = request.get_json()

            user_id = data.get('user_id', '')
            level = data.get('level', '')
            interests = data.get('interests', [])

            recommended_courses = []

            for course in courses:
                if (course['level'] == level or level == "Any") and any(interest.lower() in course['category'].lower() for interest in interests):
                    recommended_courses.append(course)

            return jsonify(recommended_courses)

        except Exception as e:
            logger.error(f"Error recommending courses: {str(e)}")
            return {'error': 'Internal server error'}, 500

api.add_resource(CourseRecommendation, '/recommend')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)
