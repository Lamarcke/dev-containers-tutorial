from flask import Flask
from services import redis_connect, mongodb_connect

app = Flask(__name__)


@app.route('/')
def hello():
    redis = redis_connect()
    redis.ping()
    mongo = mongodb_connect()
    return "Services are working!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
