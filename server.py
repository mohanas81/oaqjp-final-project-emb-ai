""" Emotion Detection Flask Application.
    This module provides a Flask-based web application for emotion detection
    using Watson NLP API. It analyzes text input and returns emotion scores
    along with the dominant emotion.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
# Initiate the flask app
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze emotion from text input.
    
    This endpoint receives text via query parameter 'textToAnalyze',
    processes it through the emotion_detector module, and returns
    emotion scores with the dominant emotion.
    
    Returns:
        str: Formatted string containing emotion scores and dominant emotion,
             or error message if text is invalid.
    
    Example:
        GET /emotionDetector?textToAnalyze=I am happy
        Returns: "For the given statement the system response is 
                  'anger': 0.001, 'disgust': 0.002, ..."
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    print(type(response))

    # Extract emotion scores
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if dominant_emotion is None (invalid input)
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Return formatted response
    return (
        f"For the given statement the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy}, "
        f"'sadness': {sadness}, "
        f"'dominant_emotion': {dominant_emotion}")


@app.route("/")
def render_index_page():
    """
    Render the main index page.
    
    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
