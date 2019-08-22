from flask import Flask, redirect, request

app = Flask(__name__)

@app.route("/")
def home():
    if request.method == 'GET':
      return "Success!! Hello, I am living in your local machine"
    else:
        return "Hello, World!"
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(debug=True)