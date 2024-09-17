from flask import Flask, request, jsonify

app = Flask(__name__)

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
            return jsonify({"message": "Transcript received successfully!"}), 200
        else:
            return jsonify({"error": "No transcript provided"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
