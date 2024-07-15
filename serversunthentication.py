# Sample credentials storage
from server import nicknames, clients, broadcast

credentials = {
    'user1': 'password1',
    'user2': 'password2'
}

# Handle client messages including authentication
def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message.startswith('REGISTER'):
                _, username, password = message.split()
                if username in credentials:
                    client.send('Username already exists!'.encode('utf-8'))
                else:
                    credentials[username] = password
                    client.send('Registered successfully!'.encode('utf-8'))
            elif message.startswith('LOGIN'):
                _, username, password = message.split()
                if credentials.get(username) == password:
                    nicknames.append(username)
                    clients.append(client)
                    client.send('Login successful!'.encode('utf-8'))
                else:
                    client.send('Invalid credentials!'.encode('utf-8'))
            else:
                broadcast(message.encode('utf-8'))
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break
