# Bios-Pentest
## EASY
1) Leap year using one line python code
This blog in one line python code helped me alot: https://blog.finxter.com/python-one-liners/ .
> f = lambda x: print("leap year" if ((x%400==0) or (x%100!=0) and (x%4==0)) else 'not leap year')
![image](https://user-images.githubusercontent.com/109974757/201533962-240b8ecc-596f-4304-8226-a212ea9c6586.png)
![image](https://user-images.githubusercontent.com/109974757/201533975-8100d9f6-6a0f-41fd-9246-3926515a3956.png)


## HARD
2) Using SELENIUM for automating file upload in a website using python .

Refered several several blogs and websites which would fill the read me files just with the links so havent added any...but there a shot notes describing the functionality of each of the element used in the the code, as a beginner as making notes side by side
>![image](https://user-images.githubusercontent.com/109974757/201534667-9f284ff6-afe4-4c89-9b43-e3b505a6095c.png)
>
>output:
>![image](https://user-images.githubusercontent.com/109974757/201535083-5659cfd5-4cb5-49ac-ab12-b49822e069e0.png)



## MEDIUM
3)chat application using socket programming
### *server side**
 
 >import socket
import threading

HOST = '127.0.0.1'
PORT = 1234 # You can use any port between 0 to 65535
LISTENER_LIMIT = 5
active_clients = [] # List of all currently connected users

### Function to listen for upcoming messages from a client
def listen_for_messages(client, username):

    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            
            final_msg = username + '~' + message
            send_messages_to_all(final_msg)

        else:
            print(f"The message send from client {username} is empty")


### Function to send message to a single client
def send_message_to_client(client, message):

    client.sendall(message.encode())

### Function to send any new message to all the clients that are currently connected to this server
def send_messages_to_all(message):
    
    for user in active_clients:

        send_message_to_client(user[1], message)

### Function to handle client
def client_handler(client):
    
    # Server will listen for client message that will
    # Contain the username
    while 1:

        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            prompt_message = "SERVER~" + f"{username} added to the chat"
            send_messages_to_all(prompt_message)
            break
        else:
            print("Client username is empty")

    threading.Thread(target=listen_for_messages, args=(client, username, )).start()

### Main function
def main():

    # Creating the socket class object
    # AF_INET: we are going to use IPv4 addresses
    # SOCK_STREAM: we are using TCP packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Creating a try catch block
    try:
        # Provide the server with an address in the form of
        # host IP and port
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    # Set server limit
    server.listen(LISTENER_LIMIT)

    # This while loop will keep listening to client connections
    while 1:

        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")

        threading.Thread(target=client_handler, args=(client, )).start()


if __name__ == '__main__':
    main()
    
    
### *client side*
>![image](https://user-images.githubusercontent.com/109974757/202889480-feb98850-3dab-4344-8909-449ee6ef954e.png)
![image](https://user-images.githubusercontent.com/109974757/202889488-4e88a84c-6d9a-4302-bf86-dc48c34fc8ee.png)

###result
>![chat ss](https://user-images.githubusercontent.com/109974757/202889530-67da263b-2100-4aa6-aa49-71c763efc745.png)
