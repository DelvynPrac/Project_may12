from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

facts = [
    "Earth is the only planet known to support life.",
    "70% of Earth's surface is covered by water.",
    "Earth's core is as hot as the Sun’s surface.",
    "A day on Earth is 24 hours long.",
    "Earth has a powerful magnetic field."
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fact')
def get_fact():
    return jsonify({"fact": random.choice(facts)})

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get("question")

    # Placeholder (we'll replace with AI later)
    response = f"You asked: {user_question}. AI response coming soon!"

    return jsonify({"answer": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4500)
