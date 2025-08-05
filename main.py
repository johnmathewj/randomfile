from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai

client = genai.Client(api_key="AIzaSyBc70X28NtqrbzEpkz6uKcbLfXgDZ1Sixs")
user_class=11

def question(topic, user_class):
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=f"Create an javascript objects containing question on the topic {topic} of {user_class}th class as the latest syllabus of CBSE, print only the object nothing else (not even comments)",
    )
    return response.text

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5500"])  # Allow only your frontend origin

@app.route('/', methods=['GET'])
@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    topic = data.get('value')
    print("Received topic:", topic)
    questions = question(topic, user_class)
    return jsonify({'topic': topic, 'questions': questions})

if __name__ == '__main__':
    app.run(debug=True)
