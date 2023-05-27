from marshmallow import Schema, fields, validate, post_load, ValidationError

class PlainTaskSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    estimated_time = fields.Integer(required=True)
    completed_time = fields.Integer(required=False)
    type = fields.String(required=True, validate=validate.OneOf(['todo', 'doing', 'done']))
    priority = fields.String(required=True, validate=validate.OneOf(['low', 'medium', 'high']))
    completed = fields.Boolean(required=True, default=False)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)


class TaskSchema(PlainTaskSchema):
    categories = fields.Nested('CategorySchema', many=True, exclude=('tasks',))



class PlainCategorySchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(required=False)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)

class CategorySchema(PlainCategorySchema):
    tasks = fields.Nested('TaskSchema', many=True, exclude=('categories',))