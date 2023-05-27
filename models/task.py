from connections.db import db


class TaskModel(db.Model): # type: ignore
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    estimated_time = db.Column(db.Integer, nullable=False)
    completed_time = db.Column(db.Integer, nullable=True)
    type = db.Column(db.String(5), nullable=False)
    priority = db.Column(db.String(6), nullable=False, default='low')
    completed = db.Column(db.Boolean,  nullable=True, default=False)
    created_at = db.Column(db.DateTime, nullable=True, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)

    # User
    # Categories
    categories = db.relationship('CategoryModel', secondary='task_category', lazy='subquery', backref=db.backref('tasks', lazy=True), cascade="all, delete")

    def __repr__(self):
        return f'<Task {self.title}>'
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self) -> None:
        self.deleted_at = db.func.current_timestamp()
        db.session.commit()
    
    @classmethod
    def find_by_id(cls, id: int) -> "TaskModel":
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_by_title(cls, title: str) -> "TaskModel":
        return cls.query.filter_by(title=title).first()
    
