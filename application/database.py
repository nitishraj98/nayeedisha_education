from application import app
from application.config import parseConfig
from flask_jwt_extended import JWTManager
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields




mysqlNayeedisha = parseConfig("nayeedishadb","/home/nitish/Documents/NayeeDisha/nayeedisha.conf","=","mysql")


print(
f'mysql+pymysql://{mysqlNayeedisha.username}:{mysqlNayeedisha.password}:{mysqlNayeedisha.host}/{mysqlNayeedisha.database}')


app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{mysqlNayeedisha.username}:{mysqlNayeedisha.password}@{mysqlNayeedisha.host}/{mysqlNayeedisha.database}'

app.config['SQLALCHEMY_BINDS'] = {
'nayeedishadb': f'mysql+pymysql://{mysqlNayeedisha.username}:{mysqlNayeedisha.password}@{mysqlNayeedisha.host}/{mysqlNayeedisha.database}'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize SQLAlchemy and Marshmallow and jwtmanager
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)















