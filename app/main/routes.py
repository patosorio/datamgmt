from . import main
from .. import db

@main.route('/')
def index():
    return "Hello, World!"