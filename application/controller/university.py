from application.controller import *


def University_Details():
    university_details = UniversityDetails.query.all()
    schema = UniversityDetailsSchema(many=True)
    result = schema.dump(university_details)
    
    return json.jsonify(result)



def add_university():
    data = request.json

    last_uid = db.session.query(UniversityDetails).order_by(UniversityDetails.uid.desc()).first()
    data['uid'] = int(last_uid.uid)+1
    
    new_university = UniversityDetails(**data)
    db.session.add(new_university)
    db.session.commit()

    ranking = Ranking(**data)
    db.session.add(ranking) 
    db.session.commit()

    news = News(**data)
    db.session.add(news)
    db.session.commit()  
       

    collaboration = Collaboration(**data)
    db.session.add(collaboration)
    db.session.commit()
    db.session.flush() 

    university_schema = UniversityDetailsSchema()
    ranking_schema = RankingSchema()
    news_schema = NewsSchema()
    collaboration_schema = CollaborationSchema()

    result1 = university_schema.dump(new_university) 
    result2 = ranking_schema.dump(ranking)
    result3 = news_schema.dump(news)
    result4 = collaboration_schema.dump(collaboration)
    

    return json.jsonify({"message":'University added successfully',"university":result1,"Ranking":result2,"News":result3,"Collaboration":result4})


def add_course():
    data = request.json
     
    data['uid'] = data.pop("add")
    last_cid = db.session.query(Courses).order_by(Courses.cid.desc()).first()
    data['cid'] = int(last_cid.cid)+1

    course = Courses(**data)
    db.session.add(course)
    db.session.commit()
    data.pop("uid") 

    fee = Fees(**data)
    db.session.add(fee)
    db.session.commit()

    prospect = Prospect(**data)  
    db.session.add(prospect)
    db.session.commit()
    db.session.flush()

    course_schema = CoursesSchema()
    fee_schema = FeesSchema()
    prospect_schema = ProspectSchema()
 
    result1 = course_schema.dump(course)
    result2 = fee_schema.dump(fee)
    result3 = prospect_schema.dump(prospect)

    return json.jsonify({"message":'Course added successfully',"Courses":result1,"Fees":result2,"Prospect":result3}) 
    