from application.models import *


class Collaboration(db.Model):
    __tablename__ = 'intcollaboration'
    icid = Column(Integer, primary_key=True)
    name = Column(String(collation="utf8mb4_0900_ai_ci"))
    link = Column(String(collation="utf8mb4_0900_ai_ci"))
    uid  = Column(Integer)
    since = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    status = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    priority = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    


class CollaborationSchema(ma.Schema):
    default_error_messages = {
        "required": "Missing data for required field.",
        "null": "Field may not be null.",
        "validator_failed": "Invalid value.",
    }
    icid  = fields.Int()
    name = fields.Str()
    link = fields.Str()
    uid = fields.Int()
    since = fields.Str()
    status = fields.Str()
    priority = fields.Str()

 



