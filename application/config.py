from application import app
from configparser import ConfigParser

class parseConfig:
    def __init__(self,context,config_path,delimeter,app):
        config = ConfigParser(delimiters=(delimeter))
        config.read(config_path)
        if app == 'mysql':
            self.database = config.get(context,'database')
            self.username = config.get(context,'username')
            self.password = config.get(context,'password')
            self.host = config.get(context,'host')
            

        if app == 'misc':
            self.jwt_key = config.get(context, 'jwt_key')
            self.secret_key = config.get(context,'secret_key')
jwt_secret = parseConfig("general","/home/nitish/Documents/NayeeDisha/nayeedisha.conf","=","misc")

app.config.update(
    TESTING = True,
    DEBUG=True,
    FLASK_ENV='development',
    JWT_BLACKLIST_ENABLED=True,
    JWT_BLACKLIST_TOKEN_CHECKS='access',
    MAIL_DEBUG=True,
    CORS_HEADERS="Content-Type", 
    JWT_SECRET_KEY=jwt_secret.jwt_key,
    SECRET_KEY=jwt_secret.secret_key


)






