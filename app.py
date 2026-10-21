from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/generate-ppt', methods=['POST'])
def generate_ppt():
    data = request.json
    # Di sini nantinya kita akan memanggil fungsi dari ppt-master
    # Untuk sementara, kita buat simulasi respon sukses
    return jsonify({"status": "success", "message": "API siap menerima data risalah project!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
