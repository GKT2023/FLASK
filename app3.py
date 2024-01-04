from flask import Flask, render_template, request, redirect,url_for

## render_template is used to redirect to html page
# redirect s used to redirect to existing route in a same app
# url_for is used to provide the url of a route
# request is use to check request is either GET or POST

app = Flask(__name__)

@app.route('/')
def home():
    return "welcome to home page"

@app.route("/success/<int:score>")  ## <int: score> is  a parameter after result in url and its type is int.
def success(score):
    return "the person is pass and the score is: " + str(score)

@app.route("/failure/<int:score>")  ## <int: score> is  a parameter after result in url and its type is int.
def failure(score):
    return "the person is fail and the score is: " + str(score)

@app.route("/calculate", methods = ['POST','GET'])  ## <int: score> is  a parameter after result in url and its type is int.
def calculate():
    result_dict = {}
    if request.method == 'GET':
        return render_template('calculate.html')
    else:
        ## retrieve field information
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        average_marks = (maths + science + history) / 3
        result_dict['Maths'] = maths
        result_dict['Science'] = science
        result_dict['History'] = history

        result = ""
        
        if average_marks >= 50:
            result = "success"
            
        else:
            result = "failure"
            
        
        # return redirect(url_for(result,score = average_marks))   ## score is the parameter which we have used to provide marks in success and  failure routes.
        ##to display marks , i will create another html

        return render_template('result.html', results=average_marks, result_dict =result_dict)    ## render to result.html
    



if __name__ == "__main__":
    app.run(debug=True)
