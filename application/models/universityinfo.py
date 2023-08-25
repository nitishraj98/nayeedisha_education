from application.models import *


class UniversityDetails(db.Model):
    __tablename__ = 'university'
    uid = Column(Integer, primary_key=True)
    name = Column(String(100,collation="utf8mb4_0900_ai_ci"))
    city = Column(String(50,collation="utf8mb4_0900_ai_ci"))
    state = Column(Integer)
    pincode = Column(String(50,collation="utf8mb4_0900_ai_ci"))
    street = Column(String(collation="utf8mb4_0900_ai_ci"))
    aboutuniversity = Column(String(collation="utf8mb4_0900_ai_ci"))
    status = Column(Integer)
    typeofuniversity = Column(String(50,collation="utf8mb4_0900_ai_ci"))
    ugcapproved = Column(Integer)
    debapproved = Column(Integer)
    decapproved = Column(Integer)
    aiuapproved = Column(Integer)
    facts	 = Column(String(collation="utf8mb4_0900_ai_ci"))
    minfees = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    maxfees = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    minduration = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    maxduration = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    priority = Column(Integer)
    shortdescription = Column(Text(collation="utf8mb4_0900_ai_ci"))
    aicteapproved = Column(Integer)
    naacrating = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    naaccgpa = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    estb = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    refundpolicy = Column(String(collation="utf8mb4_0900_ai_ci"))
    otherpolicies = Column(String(collation="utf8mb4_0900_ai_ci"))
    currentadmissionsession = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    currentadmissionsessionstatus = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    nextadmissionsession = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    nextadmissionsessionstatus = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    placement = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    policytype = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    dprating = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    strating = Column(String(45,collation="utf8mb4_0900_ai_ci"))
    scholarshipavailable = Column(Integer)
    emifacilityavailable = Column(Integer)



 
 
class UniversityDetailsSchema(ma.Schema):
    default_error_messages = {
        "required": "Missing data for required field.",
        "null": "Field may not be null.",
        "validator_failed": "Invalid value.",
    }
    uid = fields.Int()
    name = fields.Str()
    city = fields.Str()
    state = fields.Int()
    pincode = fields.Str()
    street = fields.Str()
    aboutuniversity = fields.Str()
    status = fields.Int()
    typeofuniversity = fields.Str()
    ugcapproved = fields.Int()
    debapproved = fields.Int()
    decapproved = fields.Int()
    aiuapproved = fields.Int()
    facts	 = fields.Str()
    minfees = fields.Str()
    maxfees = fields.Str()
    minduration = fields.Str()
    maxduration = fields.Str()
    priority = fields.Int()
    shortdescription = fields.Str()
    aicteapproved = fields.Int()
    naacrating = fields.Str()
    naaccgpa = fields.Str()
    estb = fields.Str()
    refundpolicy = fields.Str()
    otherpolicies = fields.Str()
    currentadmissionsession = fields.Str()
    currentadmissionsessionstatus = fields.Str()
    nextadmissionsession = fields.Str()
    nextadmissionsessionstatus = fields.Str()
    placement = fields.Str()
    policytype = fields.Str()
    dprating = fields.Str()
    strating = fields.Str()
    scholarshipavailable = fields.Int()
    emifacilityavailable = fields.Int()

