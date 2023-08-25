from flask import Flask, request, jsonify,json
from application.database import db
from datetime import datetime
import bcrypt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from application.models.universityinfo import UniversityDetails,UniversityDetailsSchema
from application.models.ranking import Ranking,RankingSchema
from application.models.news import News,NewsSchema
from application.models.blogs import Blogs,BlogsSchema
from application.models.collaboration import Collaboration,CollaborationSchema
from application.models.fees import Fees,FeesSchema
from application.models.course import Courses,CoursesSchema
from application.models.prospect import Prospect,ProspectSchema
from application.models.users import Users,UsersSchema
