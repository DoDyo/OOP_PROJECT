from flask import *
from persistenceThree import *





appThree = Flask(__name__)
appThree.config.from_mapping(
    SECRET_KEY='dev'
)


@appThree.route('/', methods=('GET', 'POST'))
def firstInput():

    if request.method == 'POST':
        w = request.form['weight']
        h = request.form['height']

        session["bmi"]=str(float(w)/(float(h)*float(h)))


        return redirect(url_for('nextplease'))

    return render_template('Input.html',)


@appThree.route('/nextPlease', methods=('GET', 'POST'))
def nextplease():
    print('Next yesss')

    bmiFloat = float(session["bmi"])
    resulttext = ''

    if bmiFloat <= 18.5:
        resulttext = 'Low but dangerous risk.'

    elif 18.5<=bmiFloat<=22.9:
        resulttext = 'Low risk. Its a good sign to be have normal weight is to show that you are at a low risk of getting diseases.'


    elif 23<=bmiFloat<=27.4:
         resulttext = 'Moderate risk'


    elif bmiFloat >= 27.5:
         resulttext = 'High risk'
    else:
        print('Try again')

 #    if request.method == 'POST':
 #       w = request.form['weight']
  #      h = request.form['height']
     #     cal = w/(h*h)
        #get the height
        #calculate the BMI, and store in variable
        #send the variable to this method below.

    return render_template('InputH.html', resulttext=resulttext, bmiFloat=bmiFloat)

@appThree.route("/123123123")
def beginner():
    return render_template("Beginner.html")

@appThree.route('/BlackPanther')
def video():
    return render_template('Video.html')







if __name__ == '__main__':
    appThree.run(debug=True)
    appThree.run(port=80)
