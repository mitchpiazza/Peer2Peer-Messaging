import socket
import os
import threading

def receive(connection):
    while True:
        buff = connection.recv(4096)
        message = buff.decode()
        print("Friend: " + message)


print("-----------------------------")
print("Would you like to connect to somebody or wait for connection?\n1 Connect to Somebody\n2 Wait for Connection")
decinput = input()
if decinput == str(1):
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    path = os.getcwd()
    print("-----------------------------")
    print("To Connect, Use \"connect <IP Address> <Port Number>\"")
    connectflag = False
    while True:
        cmd_input = input()
        if cmd_input.split(' ')[0] == "connect" and connectflag == False:
            client.connect((cmd_input.split(' ')[1], int(cmd_input.split(' ')[2])))
            connectflag = True
            t1 = threading.Thread(target=receive, args=(client,))
            t1.start()
            print("-Connected to another person!")
            print("-----------------------------")
            print("-Send messages by typing into the command line!\n-Ctrl-C to quit")
        
        if cmd_input.split(' ')[0] != "connect":
            client.sendall(bytes(cmd_input, 'UTF-8'))
            #print("You: " + cmd_input)
       
elif decinput == str(2):
    LOCALHOST = "127.0.0.1"
    PORT = 8085
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((LOCALHOST, PORT))
    server.listen(10)
    print("Waiting for peer to connect")
    msg = ''
    path = os.getcwd()
    clientConnection, clientAddress = server.accept()
    print("Connected peer :", clientAddress)
    t1 = threading.Thread(target=receive, args=(clientConnection,))
    t1.start()
    while True:
        msginput = input()
        clientConnection.send(bytes(msginput, "UTF-8"))
        #print("You: " + msginput)

    print("Peer disconnected...")
    clientConnection.close()
