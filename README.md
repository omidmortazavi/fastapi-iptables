# iptables FastAPI Client example

This repository contains a FastAPI server implementation that provides endpoints for managing iptables chains. The server allows you to get all tables, add a chain to a table, and delete a chain from a table using the provided API endpoints.

## Getting Started

To use the iptables FastAPI client with the server code, follow the steps below:

### Prerequisites

- Python 3.6 or above
- Poetry package manager (install using the instructions at https://python-poetry.org/docs/#installation)

### Running the Server

1. Clone the repository and navigate to the project directory.

2. Install the project dependencies using Poetry. Run the following command:

   ```bash
   poetry install
   ```

   This will create a virtual environment and install the required packages.

3. Start the server by running the following command:

   ```bash
   poetry shell
   $(which uvicorn) main:app --reload
   ```

   This will start the FastAPI server on `http://localhost:8000`.

### Using the Client

To test the server endpoints, you can use the provided client script `client.py`. The client script utilizes the `requests` library to make HTTP requests to the server.

1. Open a terminal and navigate to the project directory.

2. Run the client script using the following command:

   ```bash
   poetry run python client.py
   ```

   The script will perform the following operations:

   - Get all tables
   - Add a chain to the specified table
   - Get tables after adding the chain
   - Delete the chain from the table
   - Get tables after deleting the chain

   The script will display the request details, response status code, and JSON response for each operation.

3. Verify your operations on iptables with the following:
   ```bash
   iptables --list-rules #nftables
   OR
   iptables-legacy --list-rules #original iptables framework
   ```
4. Modify the client script as needed to test different scenarios or customize the operations.


## Swagger Documentation
The API documentation is available in Swagger format and can be accessed by following these steps:

Start the server by running the command mentioned in the "Running the Server" section.

Open a web browser and navigate to http://localhost:8000/docs.

This will display the Swagger UI, which provides an interactive interface to explore and test the available API endpoints. You can view details about the endpoints, parameters, request/response examples, and even make test requests directly from the Swagger UI.


## API Endpoints

The following API endpoints are provided by the server:

- `GET /tables/`: Get all tables.
- `PUT /add-chain/{table}/{chain}`: Add a chain to the specified table.
- `DELETE /delete-chain/{table}/{chain}`: Delete the specified chain from the table.
- `/`: Root endpoint to redirect users to the documentation.

## Documentation

The API documentation can be accessed by navigating to `http://localhost:8000/docs` in your web browser after starting the server. The documentation provides detailed information about the available endpoints, their parameters, and responses.