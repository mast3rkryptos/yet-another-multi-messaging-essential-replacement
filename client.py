import re
import socket
import Tkinter as tk

from ScrolledText import ScrolledText
from Tkinter import *

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"


# TODO
# - Output to log file

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


class ClientApplication(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N + tk.S + tk.E + tk.W)
        self.menu = Menu()
        self.textDisplay = ScrolledText(state='disabled')
        self.textEntry = Entry()
        self.send = Button()
        self.create_widgets()

    def create_widgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Menu
        fileMenu = Menu(self.menu)
        fileMenu.add_command(label='Configure', command=configure)
        fileMenu.add_command(label='Connect', command=connect)
        self.menu.add_cascade(label='File', menu=fileMenu)
        top.config(menu=self.menu)

        # Text Display
        self.textDisplay.grid(row=0, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

        # Text Entry
        self.textEntry.bind('<Return>', send_event)
        self.textEntry.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        # Send button
        self.send = Button(text="Send", command=send)
        self.send.grid(row=1, column=1, sticky=tk.N + tk.S + tk.E + tk.W)


def configure():
    print "Configure"


def connect():
    print "Connect"


def send():
    print "Send"
    self.textDisplay.


def send_event(event):
    send()


if __name__ == "__main__":
    ca = ClientApplication()
    ca.master.title('YAMMER')
    ca.mainloop()
