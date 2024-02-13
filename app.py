from flask import Flask, request, jsonify
from models import Ticket

tk = Ticket()

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def main():
    return jsonify({ "success": "Sistema de Tickets corriendo correctamente"}), 200

@app.route('/queue')
def list_queue():
    return jsonify(tk.get_queue()), 200

@app.route('/enqueue/<name>')
def enqueue(name):
    tk.enqueue(name)
    return jsonify(tk.get_queue()), 200

@app.route('/dequeue')
def dequeue():
    tk.dequeue()
    return jsonify(tk.get_queue()), 200

if __name__ == '__main__':
    app.run()