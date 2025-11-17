from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Flask in Docker with Python 3.14!"


if __name__ == "__main__":
    # host 0.0.0.0 para aceitar conexões de fora do container
    app.run(host="0.0.0.0", port=8002, debug=True)
