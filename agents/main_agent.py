
def calculator_tool(query):
    try:
        return str(eval(query))
    except:
        return "Error"

def run_agent(user_input):
    if any(char.isdigit() for char in user_input):
        return calculator_tool(user_input)

    system_prompt = load_prompt()
    return f"{system_prompt}\n\nAI: Thinking..."


