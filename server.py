"""
Flask application for Emotion Detection.

This module contains a Flask application that utilizes an emotion detection function 
to analyze emotions based on user-provided text.
"""
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def sent_detector():
    """
    Analyzes the emotion based on the provided text.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return jsonify({'error': 'Invalid text! Please try again.'})
    return jsonify(response)

@app.route("/")
def render_index_page():
    """
    Renders the index.html template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
