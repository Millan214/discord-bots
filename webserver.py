from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def index():
    return 'hola'

def run():
    app.run(host='0.0.0.0', port=10000)
    
def keep_alive():
    server = Thread(target=run)
    server.start()