from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", message="Hello from Flask!")

@app.route("/hello")
def hello():
    return "This is a dummy Flask route!"

if __name__ == "__main__":
    app.run(debug=True)
