from flask import Flask, request, jsonify
import os
from groq import Groq

app = Flask(__name__)

client = Groq(api_key=os.environ["GROQ_API_KEY"])

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": user_message}
        ],
        temperature=0.7
    )

    reply = completion.choices[0].message.content

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)