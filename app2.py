from flask import Flask, jsonify
import requests

app2 = Flask(__name__)

# Dictionary to store processed data
processed_data = {}

# Endpoint to fetch data from an external service and process it
@app2.route('/fetch-data', methods=['GET'])
def fetch_data():
    # Example: Fetch data from a mock API (you can replace this with Shopify or another service)
    response = requests.get('https://jsonplaceholder.typicode.com/posts')  # Mock API

    if response.status_code == 200:
        data = response.json()
        
        # Process the data: Convert 'title' to UPPERCASE and add an incrementing number to 'id'
        for item in data:
            processed_data[item['id']] = {
                'title': item['title'].upper(),  # Convert to uppercase
                'id': item['id'] + 1000  # Add a series of numbers (e.g., add 1000 to each ID)
            }
        return jsonify({'message': 'Data fetched and processed successfully'}), 200
    else:
        return jsonify({'message': 'Failed to fetch data'}), 500

# Endpoint to display the processed data
@app2.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    return jsonify(processed_data), 200

if __name__ == '__main__':
    app2.run(debug=True)
