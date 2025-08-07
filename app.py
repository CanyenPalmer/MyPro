from flask import Flask, render_template, request
from openai import OpenAI
import os

client = OpenAI()  # Uses OPENAI_API_KEY from your Render env

app = Flask(__name__)

def get_golf_response(question):
    system_message = (
        "You are a professional golf coach. For every question you are asked, "
        "respond with exactly 3 concise bullet points backed by advice from top golf professionals. "
        "Only answer golf-related questions. Be clear and actionable."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": question}
        ],
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        answer = get_golf_response(question)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
