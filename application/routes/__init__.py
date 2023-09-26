from application.controller.university import *
from application.controller.usercontroller import *
from application import app

# API for university details
@app.route('/universitydetails', methods=['POST'])
def universitydetails_route():
    return University_Details() 

# API for adding university details
@app.route('/add-university', methods=['POST'])
def add_university_route():
    return add_university() 

# API for adding courses
@app.route('/add-course', methods=['POST'])
def add_course_route():
    return add_course() 

# API for login
@app.route('/login', methods=['POST'])
def login_route():
    return login() 

# API for registration
@app.route('/register', methods=['POST'])
def register_route():
    return register() 