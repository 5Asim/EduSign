import threading
from flask import Flask, request, jsonify, send_file, render_template, Response
from pipeline.text_to_audio import generate_audio_sync
from flask_cors import CORS
from pipeline.text_to_pose_scrapper import run_background_task
import os

import pickle
import cv2
import os
import mediapipe as mp
import numpy as np
import time
from pipeline.text_to_audio import generate_audio_sync
from pipeline.text_to_pose_scrapper import run_background_task

app = Flask(__name__)
CORS(app)

# Define voice options
VOICES = ['en-US-GuyNeural', 'en-US-JennyNeural']

# Endpoint to receive the transcript
@app.route('/api/transcript', methods=['POST'])
def receive_transcript():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Extract the transcript from the data
        transcript = data.get('transcript')

        if transcript:
            # For now, we'll just print the transcript to the console
            print(f"Received transcript: {transcript}")

            # You can also save the transcript to a file, database, etc.
            # For example, saving to a file:
            if os.path.exists('transcript.txt'):
                os.remove('./transcript.txt')
                print("File deleted successfully.")
            else:
                print("File does not exist.")
            with open('transcript.txt', 'w') as f:
                f.write(transcript + '\n')
             # Start background task in a new thread
            background_thread = threading.Thread(target=run_background_task)
            background_thread.start()
            
            # Return a success message
            return send_file("../pipeline/video_0.mp4", mimetype='video/mp4')
        else:
            return send_file("./hello.mp4", mimetype='video/mp4')
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/sse')
def sse():
    print("sse")
    def generate():
        while True:
            # Check if video processing is done for this client
            if os.path.exists('./pipeline/final_video.mp4'):
                # Video is ready, send the video URL to the client
                # Upload to the vercel blobs
                
                
                yield f"data: {"./final_video.mp4"}\n\n"
                print("yield done video is ready")
                break  # End the SSE stream after sending the video URL
            else:
                # Send an update that the video is still processing
                yield "data: Video still processing...\n\n"
                time.sleep(5)  # Check every 5 seconds        
    return Response(generate(), mimetype="text/event-stream")

    
@app.route('/api/download_video', methods=['GET'])
def download_video_endpoint():
    try:
        # Assuming the video is saved as 'video_0.mp4' (or the last video processed)
        return send_file("./pipeline/final_video.mp4", mimetype='video/mp4', as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Load the model
model_dict = pickle.load(open('./pipeline/model.p', 'rb'))
model = model_dict['model']

cap = cv2.VideoCapture(1)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Define label dictionary
labels_dict = {i: chr(65 + i) for i in range(26)}  # A-Z

predicted_word = ""
last_time = time.time()  # Timer to track the delay
cooldown_time = 2  # Wait time (in seconds) between each letter recognition

@app.route('/')
def index():
    return render_template('index.html')

def generate_frames():    
    global predicted_word, last_time    
    # Load the model
    model_dict = pickle.load(open('../pipeline/model.p', 'rb'))
    model = model_dict['model']

    cap = cv2.VideoCapture(1)

    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

    # Define label dictionary
    labels_dict = {i: chr(65 + i) for i in range(26)}  # A-Z

    predicted_word = ""
    last_time = time.time()  # Timer to track the delay
    cooldown_time = 2  # Wait time (in seconds) between each letter recognition
    
    while True:
        data_aux = []
        x_ = []
        y_ = []

        ret, frame = cap.read()

        if not ret:
            break

        H, W, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]  # Only process the first hand
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                x_.append(x)
                y_.append(y)

            # Normalize landmarks
            for i in range(len(hand_landmarks.landmark)):
                data_aux.append(x_[i] - min(x_))
                data_aux.append(y_[i] - min(y_))

            if len(data_aux) == 42:  # Ensure the correct feature size
                current_time = time.time()
                if current_time - last_time > cooldown_time:
                    prediction = model.predict([np.asarray(data_aux)])
                    predicted_character = labels_dict[int(prediction[0])]

                    predicted_word += predicted_character
                    last_time = current_time

        # Display the current word on the frame
        cv2.putText(frame, predicted_word, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 255), 3, cv2.LINE_AA)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/clear_word', methods=['POST'])
def clear_word():
    global predicted_word
    predicted_word = ""
    return jsonify({"status": "cleared"})

@app.route('/get_word', methods=['GET'])
def get_word():
    global predicted_word
    print(f"Current predicted word: {predicted_word}")
    return jsonify({"predicted_word": predicted_word})

# Run the server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
