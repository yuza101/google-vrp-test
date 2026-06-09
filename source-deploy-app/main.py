from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome to my world!</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
