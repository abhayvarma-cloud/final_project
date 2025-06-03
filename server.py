from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():

    emotion_text = request.args.get("textToAnalyze")
    print(emotion_text)
    response = emotion_detector(emotion_text)
   
    formatted_text ="""For the given statement, the system response is 'anger': {}, 'disgust': {}, 
    'fear': {}, 'joy': 0.9680386 and 'sadness': {}. The dominant emotion is {}.""".format(response["anger"],
    response["disgust"], response["fear"], response["joy"], response["dominant_emotion"]
    )

    if response["dominant_emotion"] == "None":
        return "Invalid text! Please try again!."
    else:
        return formatted_text
    
@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)