from flask import Flask 

app = Flask(__name__)

@app.route("/")
def home():
    return 'Home Page'

@app.route("/about")
def about():
    return "Welcome to about us page"

@app.route("/contact")
def contact_us():
    return "contact for more details and support"

if __name__=='__main__':
    app.run(debug=True)