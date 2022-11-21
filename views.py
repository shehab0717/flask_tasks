from flask.blueprints import Blueprint
from .book.views import book_bp
from .author.views import author_bp


main_bp = Blueprint('main', __name__)
main_bp.register_blueprint(book_bp)
main_bp.register_blueprint(author_bp)