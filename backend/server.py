from flask import Flask, request, jsonify, send_file
from text_audio import generate_audio_sync
from flask_cors import CORS

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
            with open('transcript.txt', 'a') as f:
                f.write(transcript + '\n')

            

            # Return a success message
            return send_file("./hello.mp4", mimetype='video/mp4')
        else:
            return send_file("./hello.mp4", mimetype='video/mp4')
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Convert to Audio:
@app.route('/api/transcript/audio', methods=['POST'])
def transcriptToaudio():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Extract the transcript from the data
        transcript = data.get('transcript')

        if transcript:
            # Call the function to generate audio
            generate_audio_sync(transcript, VOICES[1])

            # Send the audio file back to the client
            return send_file("test.mp3", mimetype='audio/mp3')
        else:
            return jsonify({"error": "No transcript provided"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

# Run the server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
