from flask import Flask
app = Flask(__name__)
@app.route('/', methods =["POST","GET"])
def home():
    test = 
    return "Hello World !" + __name__