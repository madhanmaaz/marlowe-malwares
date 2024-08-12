from flask import Flask, request

app = Flask(__name__)

# Define the route to handle POST requests at the root URL
@app.post("/")
def root():
    # Extract the 'info' field from the JSON data in the request
    data = request.json['info']

    # Open a file named "target_information.txt" in write mode
    with open("target_information.txt", "w") as file:
        # Write the extracted data to the file
        file.write(data)

    # Return a response indicating the operation was successful
    return "OK"

# Run the Flask app on port 3000
if __name__ == "__main__":
    app.run(port=3000)
