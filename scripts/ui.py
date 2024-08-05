from tkinter import *
from scripts.chatbot import asking_chatbot


class App:
    def __init__(self, root = Tk()):
        self.root = root
        self.root.title("Weather Chatbot")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.widgets()
        self.root.mainloop()
        
    def widgets(self):
        chatlog = Text(self.root, bd=0, bg="white", height=8, width=50, font="Arial")
        chatlog.config(state=DISABLED)
        scrollbar = Scrollbar(self.root, command=chatlog.yview, orient="vertical")
        chatlog['yscrollcommand'] = scrollbar.set

        sendbutton = Button(self.root, font=("Verdana", 12, "bold"), text="Send", width=12, height=5, bd=0, bg="#32de97",
                            activeforeground="#3c9d9b", fg="#ffffff", command=send)

        promptbox = Text(self.root, bd=0, bg="white", width=29, height=5, font="Arial")
        promptbox.bind("<Return>", send)

        scrollbar.place(x=376, y=6, height=386)
        chatlog.place(x=6, y=6, height=386, width=370)
        promptbox.place(x=128, y=401, height=90, width=265)
        sendbutton.place(x=6, y=401, height=90)
            
        def check_prompt(message):
            if message != 0:
                return True

        def send():
            message = promptbox.get("1.0", 'end-1c').strip()
            promptbox.delete("0.0", END)
            if check_prompt():
                chatlog.config(state=NORMAL)
                chatlog.insert(END, f"You: {message} \n\n")
            chatlog.config(foreground="#442265", font=("Verdana, 12"))
            response = asking_chatbot()
            chatlog.insert(END, f"Bot: {response} \n\n")
            chatlog.config(state=DISABLED)
            chatlog.yview(END)