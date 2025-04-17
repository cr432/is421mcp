def run(user_input):
    try:
        expression = user_input.replace("what is", "").strip()
        result = eval(expression, {"__builtins__": {}})
        return {"response": f"The answer is {result}"}
    except:
        return {"response": "Sorry, I couldn't calculate that."}