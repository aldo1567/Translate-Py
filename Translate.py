from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data['text']
    target_language = data['target_language']
    source_language = data.get('source_language')  # Get the source language from the request payload, if provided

    translated = translator.translate(text, src=source_language, dest=target_language)
    translated_text = translated.text

    response = {'translated_text': translated_text}
    return jsonify(response)

if __name__ == '__main__':
    app.run()

