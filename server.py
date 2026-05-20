from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments 
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    if response['anger'] is None:
        formated_response = "Invalid text! Please try again!"
    else:
        anger_score = response['anger']
        disgust_score = response['disgust']
        fear_score = response['fear']
        joy_score = response['joy']
        sadness_score = response['sadness']
        dominant_emotion = response['dominant_emotion']
        formated_response = "For the given statement, the system response is 'anger':{}, " \
            " 'disgust':{}, 'fear':{}, 'joy':{} and 'sadness':{}. The dominant emotion is {}." \
            " ".format(anger_score,disgust_score,fear_score,joy_score,sadness_score,dominant_emotion)
    return formated_response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    #TODO
    app.run(host="0.0.0.0", port=5000)