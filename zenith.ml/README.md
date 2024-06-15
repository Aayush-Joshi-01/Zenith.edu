# Zenith.ml - Educational Platform with ML Models

Zenith.ml is an educational platform that leverages Machine Learning models to enhance user interaction and learning experiences. This repository houses various models used within the Zenith platform for tasks such as chatbot interactions and course recommendations.

## Models Overview

### 1. Chatbot Model

The chatbot model utilizes Google's Generative AI to provide conversational responses based on user prompts. It is designed to handle educational queries and engage users in interactive conversations.

- **Model**: Google's Generative AI (LLM)
- **Features**:
  - Responds to user queries about course content.
  - Provides explanations and answers based on educational materials.
  - Supports conversational interaction to enhance user engagement.

### 2. Course Recommendation Model

The course recommendation model suggests relevant courses based on user preferences such as course level and interests. It helps users discover new learning opportunities tailored to their needs.

- **Features**:
  - Recommends courses based on user-provided interests (e.g., Machine Learning, Web Development).
  - Filters courses by difficulty level (Beginner, Intermediate, Advanced).
  - Helps users explore diverse educational topics aligned with their interests.

### Repository Structure

The repository structure for `zenith.ml` typically includes the following files and directories:

- **api_request.py**: Contains the Flask-based API endpoints for integrating and utilizing the ML models within the Zenith platform.
- **models/**: Directory where model-related scripts and configurations are stored.
- **README.md**: Documentation file providing an overview of the ML models, their functionalities, and instructions for setup and usage.

## Usage

### Setup Instructions

1. **Environment Setup**:
   - Install Python 3.7+ and required dependencies (`Flask`, `Flask-RESTful`, `Flask-CORS`, `google-generativeai`, etc.).
   - Ensure necessary Python packages are installed using `pip`.

2. **Running the Application**:
   - Start the Flask server by running `python api_request.py` in your terminal.
   - The server will run locally on `http://localhost:5002` by default.

### API Endpoints

- **Chatbot API**:
  - Endpoint: `/chat`
  - Accepts user prompts and provides responses using the Google Generative AI model.
  - Handles conversational interactions and updates chat history.

- **Course Recommendation API**:
  - Endpoint: `/recommend`
  - Accepts user preferences (level, interests) and recommends relevant courses.
  - Retrieves course data and filters based on user criteria.

### Additional Notes

- Customize and extend the models and APIs according to specific educational needs and user feedback.
- Ensure proper logging and error handling mechanisms are in place to maintain application reliability and performance.

## Contributions

Contributions to improve and expand the functionality of the ML models and their integration within the Zenith platform are welcome. Please fork the repository, make your changes, and submit a pull request for review.

## License

The code and documentation in this repository are licensed under the MIT License. See `LICENSE` for more details.

---

This README provides an overview of the ML models used within Zenith.ml, focusing on enhancing educational interactions through advanced AI capabilities. Customize and adapt the platform as needed to cater to diverse educational contexts and user requirements.
