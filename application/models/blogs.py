from application.models import *


class Blogs(db.Model):
    __tablename__ = 'blog'
    title = Column(String(200,collation="utf8mb4_0900_ai_ci"))
    author = Column(String(100,collation="utf8mb4_0900_ai_ci"))
    date = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    blogid = Column(Integer,primary_key=True)
    content = Column(String(collation="utf8mb4_0900_ai_ci"))
    description = Column(String(500,collation="utf8mb4_0900_ai_ci"))
    status = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    priority = Column(Integer)
    thumbnail = Column(String(collation="utf8mb4_0900_ai_ci"))
    views = Column(Integer)
    content_key = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    thumbnail_key = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    byline = Column(String(collation="utf8mb4_0900_ai_ci"))
    robot_tags	 = Column(String(collation="utf8mb4_0900_ai_ci"))
    meta_title = Column(String(200,collation="utf8mb4_0900_ai_ci"))
    meta_description = Column(String(500,collation="utf8mb4_0900_ai_ci"))
    tags = Column(String(150,collation="utf8mb4_0900_ai_ci"))
    cat_id = Column(Integer)
    faqs = Column(Text(collation="utf8mb4_0900_ai_ci"))
    createdAt = Column(TIMESTAMP)
    slug = Column(Text(255,collation="utf8mb4_0900_ai_ci"))



 
 
class BlogsSchema(ma.Schema):
    default_error_messages = {
        "required": "Missing data for required field.",
        "null": "Field may not be null.",
        "validator_failed": "Invalid value.",
    }
    title = fields.Str()
    author = fields.Str()
    date = fields.Str()
    blogid = fields.Int()
    content = fields.Str()
    description = fields.Str()
    status = fields.Str()
    priority = fields.Int()
    thumbnail = fields.Str()
    views = fields.Int()
    content_key = fields.Str()
    thumbnail_key = fields.Str()
    byline = fields.Str()
    robot_tags	 = fields.Str()
    meta_title = fields.Str()
    meta_description = fields.Str()
    tags = fields.Str()
    cat_id = fields.Int()
    faqs = fields.Str()
    createdAt = fields.DateTime()
    slug = fields.Str()

