from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# Route to fetch a quote from ZenQuotes
@app.route('/quote', methods=['GET'])
def get_quote():
    try:
        # Fetch from ZenQuotes API
        response = requests.get("https://zenquotes.io/api/random")
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch quote", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

