import re
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"



# - Support the following commands
#   - cc: Create Channel
#   - cd: Destroy Channel
#   - cj: Join Channel
#   - cl: Leave Channel
#   - cm: Toggle Channel Mute/Unmute
#   - ca: Change Active Channel
#   - ci: Print Channel Info (ID, members)
#   - c:  Message Specific Channel
#   - um: Toggle User Mute/Unmute
#   - ui: Print User Info (ID, display name, channel memberships)
#   - a:  Announce
#   - y:  Yell
#   - w:  Whisper
#   - r:  Reply
def parse_command(user_cmd):
    p = re.compile("^/([a-zA-Z]+) ([\d\s\w]*$)")
    m = p.match(user_cmd)
    cmd = m.group(1).lower()


def parse_input(user_input):
    if user_input.startswith("/"):
        parse_command(user_input)
    else:
        # This is just standard message, send it to the active channel
        send_message(user_input)


def send_message(msg):
    print "sent: ", msg


def main():
    print "Client - Finished"
    exit()
    s = " "
    while " " in s:
        s = raw_input("Username (no spaces):")
    username = s
    print "Welcome, " + username
    while True:
        s = raw_input("-<>")
        parse_input(s)

    print "[client] Starting up"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()

    print "[client] received data:", data

#main()

# TODO
# - Output to log file