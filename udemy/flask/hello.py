from flask import Flask
app = Flask(__name__)
@app.route("/") 
def hello_world() :
    return "<p>Hello, World!</p>"
@app.route("/greet")
def greeting() :
    return "<h1>good morning</h1>"