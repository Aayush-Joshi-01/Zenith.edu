# Video Transcription API

This repository contains a Flask-based API that transcribes video files to text using the Whisper model. The API extracts audio from video files, transcribes the audio, and stores the transcription in a MongoDB database.

## Requirements

To run this application, ensure you have the following installed:

- Python 3.7+
- Flask
- Flask-RESTful
- Flask-CORS
- moviepy
- faster_whisper
- pymongo
- Werkzeug

You can install the required Python packages using pip:

```bash
pip install Flask Flask-RESTful Flask-CORS moviepy faster_whisper pymongo Werkzeug
```

## Configuration

1. **MongoDB Connection**:
   Configure the MongoDB connection string in `mongo_connection.py`:
   ```python
   connection_string = "your_connection_string_here"
   ```
   Replace `"your_connection_string_here"` with your actual MongoDB connection string.

2. **Whisper Model**:
   Ensure you have the Whisper model available. The code uses the base English model:
   ```python
   whisper_model = WhisperModel("base.en")
   ```

## Running the Application

To run the application, use the following command:

```bash
python api_request.py
```

This will start the Flask server on `http://0.0.0.0:5001`.

## API Endpoints

### POST /transcribe

This endpoint accepts a multipart form-data request with a video file and its associated MongoDB ID. It extracts audio from the video, transcribes the audio, and stores the transcription in the database.

#### Request

```http
POST /transcribe HTTP/1.1
Content-Type: multipart/form-data

id: [video mongodb id]
file: [video file]
```

- `id`: The MongoDB ID associated with the video.
- `file`: The video file to be transcribed.

#### Sample Request

```bash
curl -X POST http://localhost:5001/transcribe \
  -F 'id=666cc5390f6ecd103ba95f26' \
  -F 'file=@/path/to/your/video.mp4'
```

#### Response

```json
{
    "transcription": "transcription string"
}
```

- `transcription`: The transcribed text from the video.

### GET /transcribe

This endpoint can be used to check the status of the API.

#### Request

```http
GET /transcribe HTTP/1.1
```

#### Response

```json
{
    "status": "ok"
}
```

## Logging

The application uses Python's logging module to log information and errors. By default, it logs all information at the `INFO` level. You can configure the logging level and format as needed.

## Code Structure

- `api_request.py`: Main application file containing the Flask app, API endpoints, and transcription logic.
- `mongo_connection.py`: Module for MongoDB interactions, including fetching video data and updating transcriptions.

### Example of `TranscribeVideo` Class

```python
class TranscribeVideo(Resource):
    def get(self):
        return {"status": "ok"}

    def post(self):
        try:
            if 'file' not in request.files:
                return {'error': 'No file part in the request'}, 400

            video_id = request.form['id']
            file = request.files['file']

            if file.filename == '':
                return {'error': 'No file selected for uploading'}, 400

            if file:
                try:
                    data, is_dataindb = find_video_data(video_id)
                    filename = os.path.join("uploads", secure_filename(file.filename))
                    file.save(filename)
                    audio_buffer = extract_audio(filename)
                    transcript = transcribe(audio_buffer)
                    add_transcript(video_id, transcript)
                    return {'transcription': transcript}, 200

                except Exception as e:
                    logger.error(f"Error processing file: {str(e)}")
                    return {'error': 'Error processing file'}, 500

            return {'error': 'File not allowed'}, 400

        except Exception as e:
            logger.error(f"Error in request: {str(e)}")
            return {'error': 'Internal server error'}, 500
```

### Example of MongoDB Functions

```python
def find_video_data(id):
    data = list(videos.find({"_id": ObjectId(id)}))[0]
    if data:
        return data, True
    return None, False

def add_transcript(video_id, transcript):
    data = list(videos.find({"_id": ObjectId(video_id)}))[0]
    data["Transcribe"] = transcript
    videos.update_one({"_id": ObjectId(video_id)}, {"$set": data})
```

## Notes

- Ensure that the MongoDB instance is running and accessible.
- The directory paths for saving files and extracted audio should exist or be created as needed.

This README provides an overview and basic usage instructions for the Video Transcription API. Customize and extend the application as needed for your use case.
