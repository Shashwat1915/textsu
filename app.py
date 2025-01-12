from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

# Function to tokenize text into sentences using regular expressions
def regex_tokenize_sentences(text):
    # A simple regex to split text by sentence-ending punctuation (., ?, !)
    return re.split(r'(?<=[.!?]) +', text)

# Function to summarize text
def summarize_text(text, num_sentences=3):
    sentences = regex_tokenize_sentences(text)
    return " ".join(sentences[:num_sentences])

# Route to handle summarization and render the result
@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json.get('text', '')
    if not text.strip():
        return jsonify({"error": "Text input is required."}), 400
    summary = summarize_text(text)
    return jsonify({"summary": summary})

# Route to serve the homepage
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
