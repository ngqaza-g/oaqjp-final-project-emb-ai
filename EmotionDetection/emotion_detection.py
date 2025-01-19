import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    response =requests.post(url, json = input_json, headers = headers)

    # Return None for status 400
    if response.status == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }    
    # Get the emotion dictionary from the response
    response_dict = json.loads(response.text)
    emotion_dict = response_dict["emotionPredictions"][0]["emotion"]

    # Destructure the emotion dictionary
    anger_score = emotion_dict["anger"]
    disgust_score = emotion_dict["disgust"]
    fear_score = emotion_dict["disgust"]
    joy_score = emotion_dict["disgust"]
    sadness_score = emotion_dict["disgust"]
    dominant_emotion = ""
    dominant_score = 0.0

    # Determine the dominant emotion 
    for emotion, emotion_score in emotion_dict.items():
        if emotion_score > dominant_score:
            dominant_score = emotion_score
            dominant_emotion = emotion
    
    # Return the dictionary
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
