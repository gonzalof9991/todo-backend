import os
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_smorest import Api
from flask_cors import CORS
# Import routes
from routes.task_route import blp as TaskBlp
from routes.category_route import blp as CategoryBlp
# Importamos env
from dotenv import load_dotenv
# Import BD
from connections.db import db
#Import models
import models

def create_app(db_url=None):
    app = Flask(__name__)
    # Cargar .env
    load_dotenv()
    # Configuración de Flask
    app.config["API_TITLE"] = "E-Commerce REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    # Configuración DB
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config['SECRET_KEY'] = 'secret!'
    # Inicializar DB
    db.init_app(app)
    # Migrate
    migrate = Migrate(app, db)
    # Inicializar API
    api = Api(app)
    cors = CORS(app, origins="*")
    cors.init_app(app)
    # route basic
    @app.route("/")
    def index():
        return "Hello world"
    
    # Importamos las rutas
    api.register_blueprint(TaskBlp)
    api.register_blueprint(CategoryBlp)



    return app


