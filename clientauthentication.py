from tkinter import Entry, Button, Tk

from client import client, ChatApp


class AuthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login/Register")

        self.username_entry = Entry(root)
        self.username_entry.pack()

        self.password_entry = Entry(root, show='*')
        self.password_entry.pack()

        self.login_button = Button(root, text="Login", command=self.login)
        self.login_button.pack()

        self.register_button = Button(root, text="Register", command=self.register)
        self.register_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        client.send(f'LOGIN {username} {password}'.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        if response == 'Login successful!':
            root.destroy()
            chat_root = Tk()
            ChatApp(chat_root)
            chat_root.mainloop()
        else:
            print(response)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        client.send(f'REGISTER {username} {password}'.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(response)

root = Tk()
app = AuthApp(root)
root.mainloop()
