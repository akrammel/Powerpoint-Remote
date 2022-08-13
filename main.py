from flask import Flask
import webview
import sys
import threading
from server import app
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
url = "http://" + s.getsockname()[0] + ":1234/qrcode"

def start_server():
    app.run(host='0.0.0.0', port=1234)
 
if __name__ == '__main__':

    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
    
    webview.create_window("Powerpoint Remote", url, resizable=False, width=600, height=600, background_color="#222831")
    webview.start()
    sys.exit()
