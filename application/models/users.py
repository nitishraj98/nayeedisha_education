from application.models import *


class Users(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255,collation="utf8mb4_unicode_ci"))
    email = Column(String(255,collation="utf8mb4_unicode_ci"))
    user_type  = Column(Integer)
    password = Column(String(255,collation="utf8mb4_unicode_ci"))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)


class UsersSchema(ma.Schema):
    default_error_messages = {
        "required": "Missing data for required field.",
        "null": "Field may not be null.",
        "validator_failed": "Invalid value.",
    }
    id  = fields.Int()
    name = fields.Str()
    email = fields.Str()
    user_type = fields.Int()
    password = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()



