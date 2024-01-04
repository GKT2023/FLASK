## create a simple flask application

from flask import Flask

## create flask app

app = Flask(__name__) ## __name__ tells that this app is the entry point of the program



## @app.route is used to assign the URLs

@app.route("/")  # / is used for homepage, henever i hit /, home() will get triggered. @app is a decorator
def home():
    return "Hello World!!"

@app.route('/welcome')
def welcome():
    return "Welcome To The Flask Tutorials"

@app.route('/index')
def index():
    return "Welcome To The Index Page"
    

if __name__ == '__main__': ## this is the entry point of app
    # app.run() ## runs the application
    app.run(debug=True)