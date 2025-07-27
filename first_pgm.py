import customtkinter as ctk
import webbrowser
import pyttsx3 
from gtts import gTTS
import os

engine = pyttsx3.init()

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    os.system("start temp.mp3")

def click():
    msg = entry.get().strip()
    if not msg:
        return
    chatbox.insert("end", f"You: {msg}\n")

    response = "I'm sorry, I didn't understand that.Can you ask something else?."

    if(msg =="hello") :
        speak("Welcome to our restaurant! How can I assist you today?")
        response = " Welcome to our restaurant! How can I assist you today?"
  
    elif(msg =="hi") :
        speak("Welcome to our restaurant! How can I assist you today?")
        response = " Welcome to our restaurant! How can I assist you today?"
  
    elif("menu" in msg):
        speak("We serve biryani, pizza, pasta, noodles, and desserts.")
        response = "We serve biryani, pizza, pasta, noodles, and desserts."
    
    elif("timings" in msg):
        speak("We're open from 12PM to 11PM,all days of the week.")
        response = "We're open from 12PM to 11PM,all days of the week."
    
    elif(msg == "do you offer home delivery"):
        speak("Yes, we deliver through Zomato and Swiggy")
        response = "Yes, we deliver through Zomato and Swiggy."
    
    elif("thank" in msg):
        speak("You're welcome!Let me know if you have any more questions.")
        response = "You're welcome!Let me know if you have any more questions.."
    
    elif("bye" in msg):
        speak("Thank you for visiting! Have a great day!")
        response = "Thank you for visiting! Have a great day!"
    
    elif("exit" in msg):
        speak("Thank you for visiting! Have a great day!")
        response = "Thank you for visiting! Have a great day!"
        

    chatbox.insert("end", f"Bot: {response}\n")
    chatbox.see("end")    
    speak(response)
    entry.delete(0, 'end')


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app=ctk.CTk()
app.geometry("700x600")
app.title("Restaurant Service Chatbot")


chatbox = ctk.CTkTextbox(app, width=600, height=300, font=("Arial", 14), text_color="black",fg_color="white")
chatbox.pack(pady=20)

response_label =ctk.CTkLabel(app,text="",font=("Arial",16),text_color="white")
response_label.pack(pady=30)

entry = ctk.CTkEntry(app,placeholder_text="enter message", width = 400)
entry.pack(pady=30)

button = ctk.CTkButton(app,text="send", command=click)
button.pack(pady=30)

app.mainloop()

