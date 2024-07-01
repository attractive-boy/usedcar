from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from .routes import user_route,vehicle_route
        app.register_blueprint(user_route.bp,url_prefix='/api/user')
        app.register_blueprint(vehicle_route.bp,url_prefix='/api/vehicle')
        db.create_all()

    return app

