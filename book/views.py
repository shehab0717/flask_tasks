from flask.blueprints import Blueprint
from flask_restful.reqparse import RequestParser
from flask_restful import fields, marshal_with
from .models import Book
from .. models import db
from flask import render_template
from .forms import BookCreateForm
from flask import request

book_bp = Blueprint('books', __name__, url_prefix='/books')

book_parser = RequestParser()
book_parser.add_argument('id', type=int)
book_parser.add_argument('title', type=str, help='Book title is required')
book_parser.add_argument('description')
book_parser.add_argument('author_id', type=int)

book_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'author_id': fields.Integer,

}

@book_bp.route('/all')
@marshal_with(book_fields)
def all_books():
    books = Book.query.all()
    return books, 200

@book_bp.route('/<int:id>')
@marshal_with(book_fields)
def one_book(id):
    print(id)
    book = Book.query.get(id)
    return book, 200


@book_bp.route('/new', methods=['post'])
def new_book():
    book_data = book_parser.parse_args()
    book = Book(**book_data)
    db.session.add(book)
    db.session.commit()
    return 'Created', 201


@book_bp.route('/<int:id>/update', methods=['post'])
def update_book(id):
    book = Book.query.get(id)
    updated_data = book_parser.parse_args()
    book.title = updated_data['title']
    book.description = updated_data['description']
    book.author_id = updated_data['author_id']
    db.session.commit()
    return 'Updated', 200


@book_bp.route('/create', methods=['GET'])
def book_create():
    form = BookCreateForm()
    if request.GET:
        return render_template('book/create.html', form=form)
    return render_template('book/create.html', form=form)