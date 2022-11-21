from flask.blueprints import Blueprint
from flask_restful.reqparse import RequestParser

author_bp = Blueprint('authors', __name__, url_prefix='/authors')

author_parser = RequestParser()
author_parser.add_argument('id', type=int)
author_parser.add_argument('name', type=str, help='Author name is required')


@author_bp.route('/')
def AuthorIndex():
    return "Hi from author index"

@author_bp.route('/create')
def AuthorCreate():
    return "Create new author"

