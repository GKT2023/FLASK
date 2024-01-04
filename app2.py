## create a simple flask application

from flask import Flask, redirect, url_for, render_template

# redirect will redirect to the url provided
# url_for is used to form the URL.
# render_template will render a given html page
 

## create flask app

app = Flask(__name__) ## __name__ tells that this app is the entry point of the program



## @app.route is used to assign the URLs

@app.route("/")  # / is used for homepage, henever i hit /, home() will get triggered. @app is a decorator
def home():
    return "<H1> Hello World!! </H1>"  ## we can also return in HTML tags

@app.route('/welcome')
def welcome():
    return "Welcome To The Flask Tutorials"

@app.route('/index')
def index():
    # return redirect(url_for('index'))
    return render_template('index.html')   ## to create a index.html page, first create a folder name templates in a same folder and inside 
    # that create index.html
    

if __name__ == '__main__': ## this is the entry point of app
    # app.run() ## runs the application
    app.run(debug=True)  ## debug=True should be only used in development environment, not in production environment