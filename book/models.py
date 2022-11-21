from .. models import db


class Book(db.Model):
    __tablename__='book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))