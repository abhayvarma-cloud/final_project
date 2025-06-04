"""This module provides  sentiment detection API exposer over http."""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    """This function analyzes emotions from text using a sentiment detection API."""

    emotion_text = request.args.get("textToAnalyze")
    response = emotion_detector(emotion_text)
    formatted_text =f"""For the given statement,
    the system response is 'anger': {response["anger"]},
    'disgust': {response["disgust"]}, 'fear': {response["fear"]},
    'joy':{response["joy"]} and 'sadness': \
    {response["sadness"]}. The dominant emotion is
    {response["dominant_emotion"]}."""

    if response["dominant_emotion"] == "None":
        return "Invalid text! Please try again!."

    return formatted_text

@app.route("/")
def render_index_page():
    """This function provides  access to root page"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
