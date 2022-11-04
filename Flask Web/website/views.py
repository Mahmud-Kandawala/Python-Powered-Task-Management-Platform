from flask import Blueprint #bunch of urls

views = Blueprint('views', __name__)

@views.root('/') #url (root)
def home():
    return "<h1>Test</h1>"



