import socket
import threading
from tkinter import *

# Client setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 55555))

# GUI for the chat
class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application")

        self.text_area = Text(root)
        self.text_area.pack()

        self.msg_entry = Entry(root)
        self.msg_entry.pack()

        self.send_button = Button(root, text="Send", command=self.send_message)
        self.send_button.pack()

    def send_message(self):
        message = self.msg_entry.get()
        self.text_area.insert(END, f"You: {message}\n")
        client.send(message.encode('utf-8'))
        self.msg_entry.delete(0, END)

    def receive_message(self):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                self.text_area.insert(END, f"{message}\n")
            except:
                print("An error occurred!")
                client.close()
                break

root = Tk()
app = ChatApp(root)

receive_thread = threading.Thread(target=app.receive_message)
receive_thread.start()

root.mainloop()
