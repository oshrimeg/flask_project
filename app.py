from flask import Flask, request
import json



app = Flask(__name__)


@app.route('/', methods=['POST'])
def event_log():
    data = json.loads(request.data)
    with open("github_event", "w") as file:
        file.write(data)
    return 'its works'



if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')