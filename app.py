from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Russian": "ru",
    "Arabic": "ar",
    "Punjabi": "pa",
    "Urdu": "ur"
}

@app.route("/", methods=["GET", "POST"])
def home():
    translated = ""

    if request.method == "POST":
        text = request.form["text"]
        source = request.form["source"]
        target = request.form["target"]

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

    return render_template(
        "index.html",
        languages=languages,
        translated=translated
    )

if __name__ == "__main__":
    app.run(debug=True)