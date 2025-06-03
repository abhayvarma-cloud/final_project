"""This module analyzes emotions from text using a sentiment detection API."""
import requests
import json

def emotion_detector(text_to_analyze):
    """Send text to emotion API and return detected emotion."""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=header, timeout=10)
    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    result = { "anger" : emotions["anger"],
      "disgust" : emotions["disgust"],
      "fear" : emotions["fear"],
      "joy" : emotions["joy"],
      "dominant_emotion" : max(emotions,key=(emotions.get))
    }
    return result










