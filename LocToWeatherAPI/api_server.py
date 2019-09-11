from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from LocationToWeatherAPI.main import driver

app = FlaskAPI(__name__)

@app.route("/", methods=['GET'])
def rules():
    if request.method == 'GET':
        return {}

def start():
    app.run(debug=True)

if __name__ == "__main__":
    start()
