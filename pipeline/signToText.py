from flask import Flask, render_template, Response, jsonify
from flask_cors import CORS
import pickle
import cv2
import mediapipe as mp
import numpy as np
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the model
model_dict = pickle.load(open('./model.p', 'rb'))
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

if __name__ == '__main__':
    app.run(debug=True)
