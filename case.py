from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_msg():
    return jsonify({"msg": "BC4M"})

@app.route('/health', methods=['GET'])
def health_check():
    # Burada uygulamanın sağlık durumunu kontrol eden bir mantık ekleyebilirsiniz.
    return jsonify({"status": "healthy"})

@app.route('/', methods=['POST'])
def echo_post():
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

