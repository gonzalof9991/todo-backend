"""
Blueprint en Flask Smallest se utiliza para dividir una API en multiples segmentos
"""
from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import SQLAlchemyError

from connections.db import db
from models.category import CategoryModel

from request.squemas import CategorySchema

blp = Blueprint("Categories", "catgeory", description="Operations on Category")

"""
MethodView -> Podemos crear una clase cuyos métodos se dirijan a un punto final específico.
"""


@blp.route("/categories")
class Task(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.filter_by(deleted_at=None).all()


@blp.route("/category")
class TaskList(MethodView):
    # Decorador para Schema
    @blp.arguments(CategorySchema)
    @blp.response(201, CategorySchema)
    def post(self, category_data):
        print(category_data)
        category = CategoryModel(**category_data)
        try:
            category.save_to_db()
        except SQLAlchemyError:
            abort(500, message="An error ocurred whilte inserting the task.")
        return category
