from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/process', methods=['POST'])
def process():
    return jsonify({"status": "ok", "message": "Panfleto processado com sucesso!"})

if __name__ == '__main__':
    app.run()
