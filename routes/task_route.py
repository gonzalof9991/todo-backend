"""
Blueprint en Flask Smallest se utiliza para dividir una API en multiples segmentos
"""
from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import SQLAlchemyError

from connections.db import db
from models.category import CategoryModel
from models.task import TaskModel

from request.squemas import TaskSchema

blp = Blueprint("Tasks", "task", description="Operations on items")

"""
MethodView -> Podemos crear una clase cuyos métodos se dirijan a un punto final específico.
"""


@blp.route("/tasks")
class Task(MethodView):
    @blp.response(200, TaskSchema(many=True))
    def get(self):
        return TaskModel.query.filter_by(deleted_at=None).all()


@blp.route("/task")
class TaskList(MethodView):
    # Decorador para Schema
    @blp.arguments(TaskSchema)
    @blp.response(201, TaskSchema)
    def post(self, task_data):
        print(task_data)
        categories = task_data.pop("categories")
        task = TaskModel(**task_data)
        for category in categories:
            print(category)
            category = CategoryModel.find_by_name(category["name"])
            task.categories.append(category)
        
        try:
            task.save_to_db()
        except SQLAlchemyError:
            abort(500, message="An error ocurred whilte inserting the task.")
        return task
