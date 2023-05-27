# create class CategoryModel
from connections.db import db

class CategoryModel(db.Model): # type: ignore
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, nullable=True, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)
    def __repr__(self):
        return f'<Category {self.name}>'
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        self.deleted_at = db.func.current_timestamp()
        db.session.commit()
    

    @classmethod
    def find_by_id(cls, id: int) -> "CategoryModel":
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_by_name(cls, name: str) -> "CategoryModel":
        return cls.query.filter_by(name=name).first()
