from flask import Flask, request
import json

##check

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/webhook', methods=['POST'])
def webhook():
    webhook_data = request.get_json()

    if webhook_data:
        repository_name = webhook_data.get('repository', {}).get('name', 'Unknown repository')
        pusher_name = webhook_data.get('pusher', {}).get('name', 'Unknown pusher')

        filtered_data = {
            'repository_name': repository_name,
            'pusher_name': pusher_name
        }
        with open('webhook_data.json', 'w') as f:
            json.dump(webhook_data, f, indent=4)
        return 'Webhook received and saved', 200

    return 'No data', 400

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
