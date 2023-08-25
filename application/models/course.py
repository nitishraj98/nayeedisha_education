from application.models import *


class Courses(db.Model):
    __tablename__ = 'course'
    cid = Column(Integer,primary_key=True)
    name = Column(String(100,collation="utf8mb4_0900_ai_ci"))
    specializations = Column(Text(collation="utf8mb4_0900_ai_ci"))
    minduration = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    maxduration = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    specialeligibility = Column(Text(collation="utf8mb4_0900_ai_ci"))
    objective = Column(Text(collation="utf8mb4_0900_ai_ci"))
    uid = Column(Integer)
    duration = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    totalfee = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    status = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    priority = Column(Integer)
    slid = Column(Integer)
    elid = Column(Integer)
    clid = Column(Integer)
    maxfees = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    minfees = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    prospects = Column(Text(collation="utf8mb4_0900_ai_ci"))
    learningperweek = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    mode = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    coursestartyear = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    aluminicount = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    currentenrolledcount = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    degreeawarded = Column(String(100,collation="utf8mb4_0900_ai_ci"))
    mlid = Column(Integer)

 
 
class CoursesSchema(ma.Schema):
    default_error_messages = {
        "required": "Missing data for required field.",
        "null": "Field may not be null.",
        "validator_failed": "Invalid value.",
    }
    cid = fields.Int()
    name = fields.Str()
    specializations = fields.Str()
    minduration = fields.Str()
    maxduration = fields.Str()
    specialeligibility = fields.Str()
    objective = fields.Str()
    uid = fields.Int()
    duration = fields.Str()
    totalfee = fields.Str()
    status = fields.Str()
    priority = fields.Int()
    slid = fields.Int()
    elid	 = fields.Int()
    clid = fields.Int()
    maxfees = fields.Str()
    minfees = fields.Str()
    prospects = fields.Int()
    learningperweek = fields.Str()
    mode = fields.Str()
    coursestartyear = fields.Str()
    aluminicount = fields.Str()
    currentenrolledcount = fields.Str()
    degreeawarded = fields.Str()
    mlid = fields.Int()

