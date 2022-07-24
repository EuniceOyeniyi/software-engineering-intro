from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route("/") ## decorator; A function that takes another function as an arg and return another function
# AWS: Add debug Configuration | Edit Debug configuration
def index():
    return "<p>Hello, World!</p>"

@app.route("/about")
# AWS: Add debug Configuration | Edit Debug configuration
def about():
    return "<p>about</p>"

if __name__ == "__main__":
    app.run(debug=True)