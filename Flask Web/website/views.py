from flask import Blueprint #bunch of urls

views = Blueprint('views', __name__)

@views.route('/') #url (route)
def home():
    return "<h1>Test</h1>"



