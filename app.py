from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return 'Home Page'
'''
@app.route("/about")
def about():
    return "Welcome to about us page"

#Dynamic routs

@app.route("/user/<name>")
def user(name):
    return f"This data is dedicated to {name}"

@app.route("/course/<name>/<course>")
def course(name,course):
    return f"{name} is enrolled to {course} course"


#main: url converter 

#integer convertor
@app.route("/user/<int:id>")
def user(id):
    return f'User id: {id}'

#string convertor
@app.route("/userName/<string:name>")
def userName(name):
    return f'User Name: {name}'

#float convertor
@app.route("/price/<float:amount>")
def price(amount):
    return f'Price : {amount}'

#path convertor
@app.route("/file/<path:file_path>")
def file(file_path):
    return f'{file_path} opened'

#uuid convertor

from uuid import UUID

@app.route("/student/<uuid:id>") #ddeb27fb-d9a0-4624-be4d-4615062daed4
def student(id):
    return str(id)

'''

#Query parameter

@app.route("/search")
def search():
    name = request.args.get("name",'Guest')     #'Guest is the default value
    age = request.args.get("age")
    return f"Name: {name} \nage: {age}"

if __name__=='__main__':
    app.run(debug=True)