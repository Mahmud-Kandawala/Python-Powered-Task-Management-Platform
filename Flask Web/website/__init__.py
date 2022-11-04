from flask import Flask

def create_app():
    app = Flask(__name__) #Name of the file that is ran
    app.config['SECRET_KEY'] = 'abc' #Encrypt cookies and session data

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix ='/')
    app.register_blueprint(auth, url_prefix ='/')
    
    return app