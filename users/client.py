import threading
import socket
c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("_____________________________________________________________________________")
port=6969
host=str(input("Enter IP Address "))
def connect():
    try:
        c.connect((host, port))
    except:
        print("Server Not Reachable")
        return 0 
    nickname=input("Enter Nickname ")
    c.send(nickname.encode("utf-8"))
    msg=c.recv(1024)
    print(msg.decode("utf-8"),"\n To Send Messages type [To (NickName of Receipent) : Message]\n To Exit type [!exit]")
    def client_receive():
        while True:
            try:
                message=c.recv(1024).decode("utf-8")
                print(message)
            except:
                print("\n You Are Disconnected")
                break
    def client_send():
        while True:
            try:
                message=input()
                if message.strip()=="!exit":
                    c.close()
                else:
                    c.send(message.encode("utf-8"))
            except:
                break
    r_thread=threading.Thread(target=client_receive)
    r_thread.start()
    s_thread=threading.Thread(target=client_send)
    s_thread.start()
    r_thread.join()
    print("\nPress Enter to proceed ",end="")
    s_thread.join()
    exec(open("main\\main.py").read())
connect()
x=input("\nPress Enter To Proceed")
exec(open("main\\main.py").read())