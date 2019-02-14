import socket

from threading import Thread

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20

# TODO
# log file
# chat log files
# settings files
# Three threads: connections, data, user input

connections = []

def startup():
    print "[server] Starting up"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    try:
        while 1:
            conn, addr = s.accept()
            print '[server] Connection address:', addr




def main():

    # Spin off a thread to accept new connections
    threadClient = Thread(target=startup)
    threadClient.start()
    print "Finished"

    # Spin off a thread to transceive data


    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print "[server] received data:", data
        conn.send(data)
    conn.close()


#main()
