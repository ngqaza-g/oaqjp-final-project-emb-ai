''' This is the entry point of the application'''
import json
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def home():
    ''' This function renders the index page'''
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    ''' This function analyses the text sent from the index page and returns a response '''
    # Retrieve text to be analyses
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    dominant_emotion = response["dominant_emotion"]

    # Display appropriate message when dominant emotion is None
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Process the status 200 response
    del response["dominant_emotion"]

    str_response = json.dumps(response)[1:-1]
    return f'''For the given statement, the system response is {str_response}.
            \nThe dominant emotion is {dominant_emotion}'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    