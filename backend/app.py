from flask import Flask, request, jsonify
from tools import calculator, github_tool, shell_runner
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)

@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    prompt = f"You are a router. Classify the user intent as 'calculator', 'github', or 'shell'. Input: {user_input}"
    
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    intent = res['choices'][0]['message']['content'].strip().lower()

    if "calc" in intent:
        return jsonify(calculator.run(user_input))
    elif "github" in intent:
        return jsonify(github_tool.run(user_input))
    elif "shell" in intent:
        return jsonify(shell_runner.run(user_input))
    else:
        return jsonify({"response": "I don’t understand what tool to use."})

if __name__ == "__main__":
    app.run(debug=True)