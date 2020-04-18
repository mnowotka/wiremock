from marshmallow import Schema, fields


class TodoSchema(Schema):
    userId = fields.Integer(required=True)
    id = fields.Integer(required=True)
    title = fields.String(required=True)
    completed = fields.Boolean(required=True)
