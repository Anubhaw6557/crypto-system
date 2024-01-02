import socket
import threading
s=socket.socket()
host=socket.gethostname()
port=6969
s.bind((host, port))
s.listen()
clients=[]
nicknames=[]
def new_client():
    while True:
        client,address =s.accept()
        nickname=(client.recv(1024)).decode("utf-8")
        print(client,"Connected")
        client.send(("Connected Users List "+str(nicknames)).encode('utf-8'))
        for client_t in clients:
            client_t.send((nickname+" Connected").encode("utf-8"))
        clients.append(client)
        nicknames.append(nickname)
        thread=threading.Thread(target=handle_client,args=(client,))
        thread.start()
def handle_client(h_client):
    while True:
        try:
            message=h_client.recv(1024).decode("utf-8")
            index=message.find(":")
            if index==-1:
                h_client.send("Server : Not Matching Syntax( include : )".encode("utf-8"))
                continue
            user=message[2:(message.find(":"))].strip()
            if user in nicknames:
                s_nickname=nicknames[clients.index(h_client)]
                r_nickname_index=nicknames.index(user)
                r_client=clients[r_nickname_index]
                r_client.send(("From "+s_nickname+" : "+message[index+1:]).encode("utf-8"))
            else :
                h_client.send("Server : Nickname NOT Found ".encode("utf-8"))
                continue
        except:
            index=clients.index(h_client)
            clients.remove(h_client)
            h_client.close()
            nickname=nicknames[index]
            print("error !",nickname,"LEFT")
            nicknames.remove(nickname)
            for client_t in clients:
                client_t.send((nickname+" Disonnected").encode("utf-8"))
            break
new_client()


