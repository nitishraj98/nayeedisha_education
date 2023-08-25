from application.models import *


class News(db.Model):
    __tablename__ = 'news'
    nId = Column(Integer, primary_key=True)
    title = Column(String(collation="utf8mb4_0900_ai_ci"))
    link = Column(String(collation="utf8mb4_0900_ai_ci"))
    uid  = Column(Integer)
    status = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    


class NewsSchema(ma.Schema):
    default_error_messages = {
        "required": "Missing data for required field.",
        "null": "Field may not be null.",
        "validator_failed": "Invalid value.",
    }
    nId  = fields.Int()
    title = fields.Str()
    link = fields.Str()
    uid = fields.Int()
    status = fields.Str()


 
 



