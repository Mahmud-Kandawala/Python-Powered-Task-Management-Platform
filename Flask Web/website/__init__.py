from flask import Flask

def create_app():
    app = Flask(__name__) #Name of the file that is ran
    app.config['SECRET_KEY'] = 'abc' #Encrypt cookies and session data

    return app