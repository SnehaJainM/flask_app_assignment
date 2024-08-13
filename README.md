
# Flask Data Processing API

## Overview

This Flask application provides two endpoints to fetch, process, and display data from an external service. 
The data is processed by converting text to uppercase and modifying numerical values before being stored in a dictionary. 
The processed data can then be retrieved through a separate endpoint.

## Endpoints

### 1. `/fetch-data`

- **Method:** GET
- **Description:** Fetches data from an external service (e.g., a mock API), processes the data by converting the `title` field to uppercase and adding a series of numbers to the `id` field. The processed data is stored in an in-memory dictionary.
- **Response:**
  - **200 OK:** Indicates that the data was fetched and processed successfully.
  - **500 Internal Server Error:** Indicates that there was a problem fetching data from the external service.

### 2. `/get-processed-data`

- **Method:** GET
- **Description:** Returns the processed data stored in the dictionary.
- **Response:**
  - **200 OK:** Returns the processed data in JSON format.


 **Create a virtual environment (optional but recommended):**

   python -m venv venv
   venv\Scripts\activate

**Install dependencies:**

   pip install Flask requests
 

### Running the Application

1. **Run the Flask application:**

   python app.py

2. **Access the application:**

   - Open your browser or use a tool like `curl` or Postman to access the following endpoints:

   - **Fetch and Process Data:** `http://127.0.0.1:5000/fetch-data`
   - **Get Processed Data:** `http://127.0.0.1:5000/get-processed-data`

## Example Usage

1. **Fetching and Processing Data:**

   - Navigate to `http://127.0.0.1:5000/fetch-data` to fetch and process data. The server will fetch data from an external API, process it, and store it in a dictionary.

2. **Retrieving Processed Data:**

   - Navigate to `http://127.0.0.1:5000/get-processed-data` to retrieve the processed data. You should see the data with the `title` field in uppercase and the `id` field modified.



## Dependencies

- **Flask:** A micro web framework for Python.
- **requests:** A simple, yet powerful HTTP library for Python.


