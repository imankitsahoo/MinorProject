from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

@app.route('/start_emotion_detection', methods=['GET'])
def start_emotion_detection():
    try:
        # Run the main_1.py script to start emotion detection
        result = subprocess.run(['python', 'main_1.py'], capture_output=True, text=True)
        emotions_data = json.loads(result.stdout)

        # Return detected emotions as JSON response
        return jsonify(emotions_data)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
