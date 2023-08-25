from application.models import *


class Prospect(db.Model):
    __tablename__ = 'prospect'
    pid  = Column(Integer, primary_key=True)
    sectors = Column(String(100,collation="utf8mb4_0900_ai_ci"))
    designations = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    cid = Column(Integer)
    status = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    priority = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    


class ProspectSchema(ma.Schema):
    default_error_messages = {
        "required": "Missing data for required field.",
        "null": "Field may not be null.",
        "validator_failed": "Invalid value.",
    }
    pid  = fields.Int()
    sectors = fields.Str()
    designations = fields.Str()
    cid = fields.Int()
    status = fields.Str()
    priority = fields.Str()

 



