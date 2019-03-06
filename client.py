try:
    # for Python2
    import Tkinter as tk
    import ScrolledText as tkst
except ImportError:
    # for Python3
    import tkinter as tk
    import tkinter.scrolledtext as tkst

import re

# TODO
# - Output to log file

# - Support the following commands
#   - connect: [username]
#   - configure: [Server IP Address] [Server UDP Port]
#   - cc: Create Channel
#   - cd: Destroy Channel
#   - cj: Join Channel
#   - cl: Leave Channel
#   - cm: Toggle Channel Mute/Unmute
#   - ca: Change Active Channel - MAY BE OBE WITH TABS
#   - ci: Print Channel Info (ID, members)
#   - c:  Message Specific Channel
#   - h:  Help, prints out help
#   - um: Toggle User Mute/Unmute
#   - ui: Print User Info (ID, display name, channel memberships)
#   - a:  Announce
#   - y:  Yell
#   - w:  Whisper
#   - r:  Reply

USER_NAME = ""
SERVER_IP = ""
SERVER_PORT = ""


def client_command(text):
    global USER_NAME, SERVER_IP, SERVER_PORT
    ret_val = True
    if text.startswith('/con'):
        split_text = text.split(' ')
        if len(split_text) >= 3:
            SERVER_IP = split_text[1]
            SERVER_PORT = split_text[2]
            write_to_display("Connecting to " + SERVER_IP + ":" + SERVER_PORT + "\n")
            do_connect()
        else:
            ret_val = False
    elif text.startswith('/cfg'):
        split_text = text.split(' ')
        if len(split_text) >= 2:
            USER_NAME = split_text[1]
            write_to_display("Username set to " + USER_NAME + "\n")
            do_configure()
        else:
            ret_val = False
    elif text.startswith('/h'):
        write_to_display("Local: Supported Commands:\n"
                         "Local:   Connect:             /con [server IP address] [server UDP port]\n"
                         "Local:   Configure:           /cfg [username]\n"
                         "Local:   Create Channel:      /cc [channel name]\n"
                         "Local:   Destroy Channel:     /cd [channel name]\n"
                         "Local:   Join Channel:        /cj [channel name]\n"
                         "Local:   Leave Channel:       /cl [channel name]\n"
                         "Local:   Mute/Unmute Channel: /cm [channel name]\n"
                         "Local:   Set Active Channel:  /ca [channel name]\n"
                         "Local:   Show Channel Info:   /ci [channel name]\n"
                         "Local:   Message Channel:     /c [channel name] [message]\n"
                         "Local:   Show Help:           /h\n"
                         "Local:   Mute/Unmute User:    /um [username]\n"
                         "Local:   Show User Info:      /ui [username]\n"
                         "Local:   Announce:            /a [message]\n"
                         "Local:   Yell:                /y [message]\n"
                         "Local:   Whisper:             /w [username] [message]\n"
                         "Local:   Reply:               /r [message]\n")
    else:
        ret_val = False

    return ret_val


def do_configure():
    print "Configure"


def do_connect():
    print "Connect"


def do_send():
    print "Send"
    text = str(frame.textEntry.get('1.0', tk.END)).strip()
    if text != '':
        if not client_command(text):
            write_to_display(text + '\n')
    frame.textEntry.delete('1.0', tk.END)


def send_event(event):
    do_send()


def write_to_display(text):
    frame.textDisplay.config(state=tk.NORMAL)
    frame.textDisplay.insert(tk.END, text)
    frame.textDisplay.config(state=tk.DISABLED)


root = tk.Tk()
root.title("YAMMER")
frame = tk.Frame(root)
frame.grid(sticky=tk.N + tk.S + tk.E + tk.W)
frame.winfo_toplevel().rowconfigure(0, weight=1)
frame.winfo_toplevel().columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)

# Menu
#frame.menu = tk.Menu()
#frame.menu.add_command(label='Configure', command=do_configure)
#frame.menu.add_command(label='Connect', command=do_connect)
#frame.menu.add_cascade(label='File', menu=fileMenu)
#frame.winfo_toplevel().config(menu=self.menu)

# Test Display
frame.textDisplay = tkst.ScrolledText(state=tk.DISABLED, wrap=tk.WORD)
frame.textDisplay.grid(row=0, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

# Text Entry
frame.textEntry = tkst.ScrolledText(height=5)
#self.textEntry.bind('<Shift-Return>')
frame.textEntry.bind('<Return>', send_event)
frame.textEntry.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
frame.textEntry.focus_set()

# Send Button
frame.send = tk.Button(text="Send", command=do_send)
frame.send.grid(row=1, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

root.mainloop()
