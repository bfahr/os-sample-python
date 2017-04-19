import time
from flask import Flask, json, Response


class ApiResult(object):

    def __init__(self, value, status=200):
        self.value = value
        self.status = status

    def to_response(self):
        return Response(json.dumps(self.value),
                        status=self.status,
                        mimetype='application/json',
                        headers={'Access-Control-Allow-Origin': '*'})


class ApiException(Exception):

    def __init__(self, message, status=400):
        self.message = message
        self.status = status

    def to_result(self):
        return ApiResult({'message': self.message},
                         status=self.status)


class ApiFlask(Flask):

    def make_response(self, rv):
        if isinstance(rv, ApiResult):
            return rv.to_response()
        return Flask.make_response(self, rv)


application = ApiFlask(__name__)
application.register_error_handler(
    ApiException, lambda err: err.to_result())


@application.route("/")
def hello():
    return "Hello World!"


@application.route("/algo")
def algo():
    time.sleep(10)
    results = {
        'name': 'algorithm 3',
        'input': '1.5',
        'output': 2,
        'duration': 10
    }
    return ApiResult(results)


if __name__ == "__main__":
    application.run()
