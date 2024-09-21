from flask import Flask, render_template, Response, jsonify, request, send_file

from flask_cors import CORS
from text_to_audio import generate_audio_sync
import pickle
import cv2
import mediapipe as mp
import numpy as np
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
VOICES = ['en-US-GuyNeural', 'en-US-JennyNeural']
if __name__ == '__main__':
    app.run(debug=True)
