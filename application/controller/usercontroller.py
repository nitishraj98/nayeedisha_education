from application.controller import *


def register():
    data = request.json
    
    # Check if the email already exists
    existing_user = Users.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify(message='Email already registered'), 409
     
    # Hash the password
    password_bytes = data['password'].encode('utf-8')
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode('utf-8')    
    current_datetime = datetime.now()
    create_at =  current_datetime.strftime("%Y-%m-%d %H:%M:%S") 
    update_at = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # Create a new user   
    new_user = Users(
        name=data['name'],
        email=data['email'],
        password=hashed_password,
        user_type=1, 
        created_at=create_at,
        updated_at=update_at
    ) 
    
    db.session.add(new_user)
    db.session.commit()                                                                 
    
    return jsonify(message='User registered successfully'), 200


def login():
    email = request.json['email']
    password = request.json['password']
 
    # Find the user by email
    user = Users.query.filter_by(email=email).first()

    if user:
        # Check if the password matches
        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            access_token = create_access_token(identity=email)
            
            return jsonify({'access_token': access_token,'username': user.name,
                'id': user.id,'Email':user.email,'message': 'Login successful'}),200
        else:
            return jsonify({'message': 'Invalid password'})
    else:
        return jsonify({'message': 'User not found'}), 404    
    
          