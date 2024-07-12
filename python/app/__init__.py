import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import importlib

db = SQLAlchemy()
migrate = Migrate()

def load_routes(app, package):
    package_dir = os.path.join(os.path.dirname(__file__), 'routes')
    for filename in os.listdir(package_dir):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = f"{package}.{filename[:-3]}"
            module = importlib.import_module(module_name)
            if hasattr(module, 'bp'):
                prefix = filename.split('_')[0]
                app.register_blueprint(module.bp, url_prefix=f'/api/{prefix}')
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        load_routes(app, 'app.routes')
        db.create_all()

    return app

