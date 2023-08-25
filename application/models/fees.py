from application.models import *


class Fees(db.Model):
    __tablename__ = 'fee'
    fid = Column(Integer, primary_key=True)
    name = Column(Text(collation="utf8mb4_0900_ai_ci"))
    fee = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    duration  = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    cid = Column(Integer)
    status = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    description = Column(String(100,collation="utf8mb4_0900_ai_ci"))
    priority = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    


class FeesSchema(ma.Schema):
    default_error_messages = {
        "required": "Missing data for required field.",
        "null": "Field may not be null.",
        "validator_failed": "Invalid value.",
    }
    fid  = fields.Int()
    name = fields.Str()
    fee = fields.Str()
    duration = fields.Str()
    cid = fields.Int()
    status = fields.Str()
    description =fields.Str()
    priority = fields.Str()

 



