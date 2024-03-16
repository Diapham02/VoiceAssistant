import google.generativeai as genai
import speech_recognition as sr
import pyttsx3


# Cấu hình API key
genai.configure(api_key="AIzaSyAbhBBlqCiVWjIXzc99BaXDOausFnde-RI")

# Khởi tạo model chatbot
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Khởi tạo nhận dạng giọng nói
recognizer = sr.Recognizer()

# Khởi tạo tổng hợp giọng nói
engine = pyttsx3.init()

while True:

    option = input("Nhập (1) để nhập văn bản, (2) để nhập bằng giọng nói: ")

    if option == '1':
        question = f'{input("You: ")}'

    elif option == '2':

        with sr.Microphone() as source:
            print("Nói điều bạn muốn hỏi: ")
            audio = recognizer.listen(source)

        question = recognizer.recognize_google(audio)

    # Gửi câu hỏi lên chatbot và nhận câu trả lời
    response = chat.send_message(question)

    # In ra màn hình hoặc nói ra câu trả lời
    if option == '1':
        print("Bot: {}".format(response.text))
    else:
        engine.say(response.text)
        engine.runAndWait()
