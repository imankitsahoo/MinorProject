from flask import Flask, render_template, jsonify
import json
import os
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
import cv2
import numpy as np
import time
import random

app = Flask(__name__)

# Load the pre-trained model and cascade classifier
face_classifier = cv2.CascadeClassifier(r'C:\Users\KIIT\OneDrive\Documents\MINOR Project\Backend\Emotion_Detection_CNN-main\haarcascade_frontalface_default.xml')
classifier = load_model(r'C:\Users\KIIT\OneDrive\Documents\MINOR Project\Backend\Emotion_Detection_CNN-main\model.h5')
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Video links for each emotion
video_links = {
    'Angry': [
        "https://youtu.be/e9dZQelULDk?si=tN7f_wbDsdFL78BG",
        "https://youtu.be/HM46YzlPY9E?si=eIQza8N9fsBwr6qU",
        "https://youtu.be/aL2nYsXNfMI?si=6osufTu2UNClE9IG"
    ],
    'Disgust': [],  # Add links for Disgust
    'Fear': [],     # Add links for Fear
    'Happy': [
        "https://youtu.be/9DtcSCFwDdw?si=k0O6tZWLxVeCB43m",
        "https://youtu.be/fUXdrl9ch_Q?si=H2sWzTLxPIBrqwfG",
        "https://youtu.be/78nsxRxbf4w?si=B7a28bnFXW6MhYJm"
    ],
    'Neutral': [
        "https://youtu.be/xNY0AAUtH3g?si=0wSrv0kkMx_lUCaa",
        "https://youtu.be/Uew5BbvmLks?si=3vEY54zFXwTesd6y",
        "https://youtu.be/29Vj0-TVHiQ?si=Gmry348N8sS_jcoH"
    ],
    'Sad': [
        "https://youtu.be/e9dZQelULDk?si=tN7f_wbDsdFL78BG",
        "https://youtu.be/HM46YzlPY9E?si=eIQza8N9fsBwr6qU",
        "https://youtu.be/aL2nYsXNfMI?si=6osufTu2UNClE9IG"
    ],
    'Surprise': [],  # Add links for Surprise
}

@app.route('/')
def home():
    return render_template('chat_1.html')

@app.route('/get_prediction')
def get_prediction():
    emotions_data = run_emotion_detection()
    prediction = "Unknown"
    if emotions_data:
        prediction = emotions_data[-1]  # Get the latest prediction
    recommended_videos = video_links.get(prediction, [])  # Get recommended videos based on prediction
    return jsonify({'emotion': prediction, 'recommended_videos': recommended_videos})

@app.route('/stop_scanning')
def stop_scanning():
    return 'Scanning stopped.'

def run_emotion_detection():
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    end_time = start_time + 10  # Run the detection for 10 seconds
    emotions_data = []

    while time.time() < end_time:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = np.expand_dims(roi, axis=0)

                prediction = classifier.predict(roi)[0]
                detected_emotion = emotion_labels[prediction.argmax()]
                emotions_data.append(detected_emotion)
                label_position = (x, y)
                cv2.putText(frame, detected_emotion, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                cv2.putText(frame, 'No Faces', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Emotion Detector', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    output_file = 'output.json'
    with open(output_file, "w") as outfile:
        json.dump(emotions_data, outfile, indent=4)

    return emotions_data

if __name__ == '__main__':
    app.run(debug=True)
