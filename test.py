import google.generativeai as genai
API_KEY = "AIzaSyDWgcwJH2as2dFat5guor2jOKvsavRpX-4"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")
def chat_with_gemini(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {e}"
print("AI Chatbot (Gemini): Type 'exit' to end chat")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot session ended.")
        break
    print("AI Chatbot:", chat_with_gemini(user_input))
