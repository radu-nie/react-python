from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api
from flask_cors import CORS

db = SQLAlchemy()


def create_app(env=None):
    from config import config_by_name
    from routes import register_routes
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="Radu Nie API", version="1.0")

    register_routes(api, app)
    db.init_app(app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
