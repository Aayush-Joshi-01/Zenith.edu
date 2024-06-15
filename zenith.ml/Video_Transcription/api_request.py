from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from moviepy.editor import VideoFileClip
from faster_whisper import WhisperModel
import os
import logging
import io
import wave
import numpy as np
from werkzeug.utils import secure_filename

from ..mongo_connection import find_video_data, add_transcript

app = Flask(__name__)
api = Api(app)
CORS(app)

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

whisper_model = WhisperModel("base.en")

def extract_audio(video_file):
    try:
        video = VideoFileClip(video_file,verbose=True)
        print(video_file)
        audio_path=os.path.join("audios",video_file.replace('mp4','mp3').split('\\')[1])
        video.audio.write_audiofile(audio_path)
        return audio_path
    except Exception as e:
        logger.error(f"Error extracting audio: {str(e)}")
        raise

def transcribe(audio_path):
    try:
        segments, info = whisper_model.transcribe(audio_path, vad_filter=True, 
        vad_parameters=dict(min_silence_duration_ms=500))

        transcription = "".join([segment.text for segment in segments])
        print(transcription)
        return transcription
    except Exception as e:
        logger.error(f"Error transcribing audio: {str(e)}")
        raise

class TranscribeVideo(Resource):
    """
    request
    POST /transcribe
    Content-Type: multipart/form-data
    id: [video mongodb id]
    file: [video file]

    response
    {'transcription': transcription string}
    """
    def get(self):
        return {"status":"ok"}
    def post(self):
        
        try:
            if 'file' not in request.files:
                return {'error': 'No file part in the request'}, 400

            video_id=request.files['id']
            file = request.files['file']
            

            if file.filename == '':
                return {'error': 'No file selected for uploading'}, 400

            if file:
                try:
                    video_file = io.BytesIO(file.read())

                    audio_buffer = extract_audio(video_file)
                    transcription = transcribe(audio_buffer)
                    
                    torch.cuda.empty_cache()
                    
                    return {'transcription': transcription}, 200

                except Exception as e:
                    logger.error(f"Error processing file: {str(e)}")
                    return {'error': 'Error processing file'}, 500

            return {'error': 'File not allowed'}, 400

        except Exception as e:
            logger.error(f"Error in request: {str(e)}")
            return {'error': 'Internal server error'}, 500

api.add_resource(TranscribeVideo, '/transcribe')

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)