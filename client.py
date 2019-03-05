try:
    # for Python2
    import Tkinter as tk
    import ScrolledText as tkst
except ImportError:
    # for Python3
    import tkinter as tk
    import tkinter.scrolledtext as tkst

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

def do_configure():
    print "Configure"


def do_connect():
    print "Connect"


def do_send():
    print "Send"
    text = str(frame.textEntry.get('1.0', tk.END)).strip()
    if text != '':
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
frame.bind('<Return>', send_event)
frame.textEntry.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

# Send Button
frame.send = tk.Button(text="Send", command=do_send)
frame.send.grid(row=1, column=1, sticky=tk.N + tk.S + tk.E + tk.W)

root.mainloop()
