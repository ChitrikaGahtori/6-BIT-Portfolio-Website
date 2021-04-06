from flask import Flask, render_template
app = Flask(__name__, template_folder='template') 


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('inner-page.html')


@app.route("/portfolio-details")
def contact():
    return render_template('portfolio-details.html')


@app.route("/vivek")
def vivek():
    return render_template('vivek.html')


@app.route("/rashi")
def rashi():
    return render_template('rashi.html')


@app.route("/abhishek")
def abhishek():
    return render_template('abhishek.html')


@app.route("/shivam")
def shivam():
    return render_template('shivam.html')


@app.route("/ankit")
def ankit():
    return render_template('ankit.html')


@app.route("/chitrika")
def chitrika():
    return render_template('chitrika.html')



app.run(debug=True)

