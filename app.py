from flask import Flask, render_template, request
import openai

openai.api_key = "your-api-key-here"

app = Flask(__name__)

def get_golf_response(question):
    system_message = (
        "You are a professional golf coach. For every question you are asked, "
        "respond with exactly 3 concise bullet points backed by advice from top golf professionals. "
        "Only answer golf-related questions. Be clear and actionable."
    )

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": question}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
        max_tokens=300
    )

    return response['choices'][0]['message']['content']

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        answer = get_golf_response(question)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
