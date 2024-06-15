from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from moviepy.editor import VideoFileClip
from faster_whisper import WhisperModel
import torch
import os
import logging
import io
import wave
import numpy as np

from ..mongo_connection import find_video_data, add_transcript

app = Flask(__name__)
api = Api(app)
CORS(app)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

whisper_model = WhisperModel("base.en")

def extract_audio(video_file):
    try:
        video = VideoFileClip(video_file)
        audio_buffer = io.BytesIO()
        video.audio.write_audiofile(audio_buffer, codec='pcm_s16le')
        audio_buffer.seek(0)
        return audio_buffer
    except Exception as e:
        logger.error(f"Error extracting audio: {str(e)}")
        raise

def transcribe(audio_buffer):
    try:
        with wave.open(audio_buffer, 'rb') as wf:
            audio_data = wf.readframes(wf.getnframes())
        audio_tensor = torch.FloatTensor(np.frombuffer(audio_data, dtype=np.int16)).unsqueeze(0)
        segments, info = whisper_model.transcribe(audio_tensor, vad_filter=True, vad_parameters=dict(min_silence_duration_ms=500))
        transcription = "".join([segment['text'] for segment in segments])
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
                    data,is_data_indb=find_video_data(video_id)
                    if not is_data_indb:
                        return {'error':"Video id doesnot exist in database.."}, 404
                
                    video_file = io.BytesIO(file.read())
                    audio_buffer = extract_audio(video_file)
                    transcription = transcribe(audio_buffer)
                    add_transcript(data,transcription)
                    
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
