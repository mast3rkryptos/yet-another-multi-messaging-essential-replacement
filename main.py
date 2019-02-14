# system imports
from threading import Thread

# project imports
import client
import server

if __name__ == '__main__':
    threadServer = Thread(target=server.main)
    threadClient = Thread(target=client.main)
    threadServer.start()
    threadClient.start()
    threadServer.join()
    print "Finished"
