from connections.db import db

# Tabla de unión para la relación many-to-many entre TaskModel y CategoryModel
task_category = db.Table('task_category',
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)