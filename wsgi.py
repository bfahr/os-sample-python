import time
from flask import Flask

application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello World!"


@application.route("/algo")
def algo():
    time.sleep(10)
    return "The answer is 2"


if __name__ == "__main__":
    application.run()
