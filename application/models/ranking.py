from application.models import *


class Ranking(db.Model):
    __tablename__ = 'ranking'
    rId = Column(Integer, primary_key=True)
    authority = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    rankingyear = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    ranking = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    uid  = Column(Integer)
    status = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    priority = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    description = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    


 
 
class RankingSchema(ma.Schema):
    default_error_messages = {
        "required": "Missing data for required field.",
        "null": "Field may not be null.",
        "validator_failed": "Invalid value.",
    }
    rId  = fields.Int()
    authority = fields.Str()
    rankingyear = fields.Str()
    ranking = fields.Str()
    uid = fields.Int()
    status = fields.Str()
    priority = fields.Str()
    description = fields.Str()


    

