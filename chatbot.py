import numpy as np
import re
chat_data = {
    r"(hi|hello|hey)": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
    r"(how are you)": ["I'm doing great, thanks!", "All good here. How about you?", "Feeling awesome!"],
    r"(what is your name)": ["I'm a simple chatbot.", "You can call me PyBot!", "I'm your Python friend!"],
    r"(bye|goodbye)": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
    r"(what are you doing)":["Nothing,what about you?"],
    r"(can you help me)":["yes! I can"],
    r"(what is python)":["Python is a high-level, interpreted, general-purpose programming language"],
    r"(what is numpy)":["Numpy is a Python library used for fast numerical computing."],
    r"(bahubali)":["Bahubali is a popular Indian epic action film series directed by S.S.Rajamouli"]
}

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    for pattern, responses in chat_data.items():
        if re.search(pattern, user_input):
            return np.random.choice(responses)  # NumPy random selection
    return "I'm not sure I understand you."

# Step c: Create a responding chatbot
print("Enhanced Python Chatbot. Type 'exit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Have a nice day")
        break
    print("Chatbot:", chatbot_response(user_input))

