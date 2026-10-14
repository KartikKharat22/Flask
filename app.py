from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = 'Kartik'
    course = 'AI - DS'
    age = 21
    return render_template("index.html",
                           name=name,
                           course=course,
                           age=age)

if __name__=='__main__':
    app.run(debug=True)