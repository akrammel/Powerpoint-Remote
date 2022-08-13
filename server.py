from flask import Flask, render_template
from win32.win32gui import GetWindowText, GetForegroundWindow
import keyboard

# Execute commands
def execCommand(cmd):
    wintext = GetWindowText(GetForegroundWindow())        
    #if "Google Sheets" in wintext:
    if not cmd is None:
        if   cmd == 'next':
            keyboard.send('space')
        elif cmd == 'back':
            keyboard.send('backspace')
        elif cmd == 'stop':
            keyboard.send('escape')

app = Flask(__name__)
#Remote
@app.route("/")
def remote():
    return render_template('remote.html')
#Qrcode
@app.route("/qrcode")
def qrcode():
    return render_template('qrcode.html')
#Commands
@app.route('/cmd/<cmd>')
def returnCommand(cmd):
    if cmd in ["next", "back", "stop"]:
        execCommand(cmd)
    return ""
