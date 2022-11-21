from flask import Flask
from .config import app_config
from .models import db
from .views import main_bp
from flask_migrate import Migrate

def create_app(mode):
    app = Flask(__name__)
    config = app_config[mode]
    app.config['SQLALCHEMY_DATABASE_URI'] = config
    app.config.from_object(config)
    app.register_blueprint(main_bp)
    db.init_app(app)

    migrate = Migrate(app, db)

    return app