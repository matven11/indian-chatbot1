# project config
import google.generativeai as genai

genai.configure(api_key="AIzaSyC9rmPjs1ikO_yH1lWNi8CYAFz2l2Vg_1c")

apple = genai.GenerativeModel("gemini-2.0-flash")

chat = apple.start_chat(history=[])

print("Hi MatVen, I'm GenAi")

while True:
    user_input = input("User: ")

    if user_input.strip().lower() == "bye":
        break

    response = chat.send_message(user_input)
    print("Apple:", response.text)
