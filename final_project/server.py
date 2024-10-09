"""
This module contains a Flask application for emotion detection from text input.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Route to analyze text for emotional content.
    
    Returns:
        JSON response containing the detected emotions or an error message.
    """
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    if not text_to_analyze:
        return jsonify({'error': 'No text provided'}), 400

    emotions = emotion_detector(text_to_analyze)

    if emotions['dominant_emotion'] is None:
        return jsonify({'error': 'Invalid text! Please try again!'}), 400

    response = {
        "anger": emotions['anger'],
        "disgust": emotions['disgust'],
        "fear": emotions['fear'],
        "joy": emotions['joy'],
        "sadness": emotions['sadness'],
        "dominant_emotion": emotions['dominant_emotion']
    }

    output_message = (f"For the given statement, the system response is "
                      f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
                      f"'fear': {response['fear']}, 'joy': {response['joy']}, "
                      f"'sadness': {response['sadness']}. The dominant emotion is "
                      f"{response['dominant_emotion']}.")

    return jsonify(output_message)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
