
from flask import Flask,render_template,request, jsonify

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is missing")

client = genai.Client(api_key=api_key)


app = Flask(__name__)

@app.route( "/" )
def home():
    return render_template("index.html")



@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message")
    if not message or not message.strip():
     return jsonify({"error": "Message cannot be empty"}), 400

    response = client.models.generate_content(
  model="gemini-3.8-flash",
        contents=message
    )

    return jsonify({"reply": response.text})




   





if __name__ == "__main__":
    app.run(debug=True)