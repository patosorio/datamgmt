from . import app, db

@app.route('/')
def index():
    return "Hello baby!"