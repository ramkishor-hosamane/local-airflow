from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Get the JSON payload
    print("Received Webhook:", data)  # Print it to console
    return jsonify({"message": "Webhook received"}), 200

if __name__ == '__main__':
    app.run(port=3000, debug=True)
