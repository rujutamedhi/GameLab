from flask import Flask, render_template, request, redirect, url_for,jsonify,session
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy import func
import secrets
import os
import subprocess
local_server =True
app = Flask(__name__, static_folder='static')
with open("C:\\projects\\netflix\\config.json") as c:
     params=json.load(c)["params"]
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rujutamedhi%4004@localhost/netflix'

# Set a fallback secret key or make sure the environment variable is set
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', secrets.token_hex(100))


db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phno = db.Column(db.String(20))
    password = db.Column(db.String(100))
    @staticmethod
    def get_id_by_name(username):
        global  name
        user = User.query.filter_by(name=username).first()
        if user:
            return user.id
        else:
            return None

# Create the database tables
    with app.app_context():

      db.create_all()
class Score(db.Model):
    __tablename__ = 'spaceinvadersscore'
    score_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    score = db.Column(db.Integer)
class Score1(db.Model):
    __tablename__ = 'flappybirdscore'
    score_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    score = db.Column(db.Integer)
class EggScore(db.Model):
    __tablename__ = 'eggscore'
    eggscore_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('users.id'))
    score = db.Column(db.Integer)
class snakeScore(db.Model):
    __tablename__ = 'snakescore'
    eggscore_id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey('users.id'))
    score = db.Column(db.Integer)

# Create the database tables
with app.app_context():
    db.create_all()
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/submit_egg_score', methods=['POST'])
def submit_egg_score():
    try:
        # Parse JSON data from the request
        data = request.json
        username = data.get('name')
        print(username)
        score_value = data.get('score')
        
        # Retrieve the user ID based on the username
        user_id = User.get_id_by_name(name)
        print(user_id)

        if user_id is not None:
            
            # Create a new EggScore entry with the user ID and score
            new_egg_score = EggScore(id=user_id, score=score_value)
            
            # Add the new entry to the database
            db.session.add(new_egg_score)
            db.session.commit()
            
            return jsonify({"message": "Score added successfully"}), 200
        else:
            
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        # Handle exceptions and rollback the session if an error occurs
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        # Always close the database session at the end
        db.session.close()

@app.route('/submit_snake_score', methods=['POST'])
def submit_snake_score():
    try:
        # Parse JSON data from the request
        data = request.json
        username = data.get('name')
        
        score_value = data.get('score')
        
        # Retrieve the user ID based on the username
        user_id = User.get_id_by_name(name)
        print(user_id)

        if user_id is not None:
            
            # Create a new EggScore entry with the user ID and score
            new_egg_score = snakeScore(id=user_id, score=score_value)
           
            # Add the new entry to the database
            db.session.add(new_egg_score)
            db.session.commit()
            
            return jsonify({"message": "Score added successfully"}), 200
        else:
            
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        # Handle exceptions and rollback the session if an error occurs
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        # Always close the database session at the end
        db.session.close()

@app.route('/display_highest_score')
def display_highest_score():
    highest_score = db.session.query(func.max(Score.score)).scalar()
    highest_score_user = db.session.query(User.name).join(Score).filter(Score.score == highest_score).scalar()
    highest_score1 = db.session.query(func.max(Score1.score)).scalar()
    highest_score_user1 = db.session.query(User.name).join(Score1).filter(Score1.score == highest_score1).scalar()
    highest_score2 = db.session.query(func.max(EggScore.score)).scalar()
    highest_score_user2 = db.session.query(User.name).join(EggScore).filter(EggScore.score == highest_score2).scalar()
    highest_score3 = db.session.query(func.max(snakeScore.score)).scalar()
    highest_score_user3 = db.session.query(User.name).join(snakeScore).filter(snakeScore.score == highest_score3).scalar()
    
    return render_template('dashboard.html', highest_score=highest_score, highest_score_user=highest_score_user,highest_score1=highest_score1, highest_score_user1=highest_score_user1,highest_score_user2=highest_score_user2,highest_score2=highest_score2,highest_score_user3=highest_score_user3,highest_score3=highest_score3)


@app.route('/submit_score', methods=['POST'])

def submit_score():
   
    try:
        
        data = request.json  # Get the JSON data from the request
       
        username = data.get('name')  # Extract the username from the JSON data
        
        score_value = data.get('score')  # Extract the score from the JSON data
        
        # Retrieve the user ID based on the username
        user_id = User.get_id_by_name(name)
        
        if user_id is not None:
            
            # Create a new score entry with the retrieved user ID
            score = Score(score_id=score_value,id=user_id, score=score_value)
            
            db.session.add(score)
            
            db.session.commit()
            
        
            return jsonify({"message": "Score added successfully"}), 200
        else:
            # Return an error message if user not found
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/display_highest_score1')
def display_highest_score1():
    highest_score1 = db.session.query(func.max(Score1.score)).scalar()
    highest_score_user1 = db.session.query(User.name).join(Score1).filter(Score1.score == highest_score1).scalar()
    print(highest_score_user1,highest_score1)
    return render_template('dashboard.html', highest_score1=highest_score1, highest_score_user1=highest_score_user1)

@app.route('/submit_score2', methods=['POST'])
def submit_score2():
    
    try:
        
        data = request.json  # Get the JSON data from the request
        
        username = data.get('name')  # Extract the username from the JSON data
        
        score_value = data.get('score')  # Extract the score from the JSON data
        
        # Retrieve the user ID based on the username
        user_id = User.get_id_by_name(name)
        
        if user_id is not None:
            
            # Create a new score entry with the retrieved user ID
            score = Score1(score_id=score_value,id=user_id, score=score_value)
            
            db.session.add(score)
            
            db.session.commit()
            
        
            return jsonify({"message": "Score added successfully"}), 200
        else:
            # Return an error message if user not found
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
       
# @app.route('/add_score', methods=['POST'])
# def add_score():
#     print("hiya")
#     score_data = request.json
#     score = score_data.get('score')

#     # Store the score in the database or do any other necessary processing
#     # Example: Save the score to the database
#     new_score_entry = Score(score=score)
#     db.session.add(new_score_entry)
#     db.session.commit()

#     return 'Score added successfully'
@app.route('/success')
def success():
    return 'User added successfully!'
@app.route('/check_auth', methods=['GET'])
def check_auth():
    print("Check auth endpoint hit")  # Debugging
    if 'user_id' in session:
        print("User is authenticated")  # Debugging
        return jsonify({'is_authenticated':True})
    else:
        print("User is not authenticated")  # Debugging
        return jsonify({'is_authenticated': False})

@app.route('/signin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the email and password from the form
        global name
        name = request.form['name']
        password = request.form['password']
        
        # Query the database to check if the email and password match
        user = User.query.filter_by(name=name, password=password).first()
        if user:
            session['user_id'] = user.id
            print(session['user_id'])
            
            # If a user with the provided email and password exists, redirect to index page
            return redirect(url_for('index'))
        else:
            # If no matching user found, redirect back to the login page
            return redirect(url_for('login'))

    # Render the login page template for GET requests
    return render_template('signin.html')

@app.route("/signup",methods=['GET', 'POST'])
def signup():
    
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        phno = request.form['phno']
        password = request.form['password']
        
        # Create a new user instance
        new_user = User(name=name, email=email, phno=phno, password=password)
        
        # Add the new user to the database session
        db.session.add(new_user)
        
        # Commit the session to the database
        db.session.commit()
        
        return redirect(url_for('success'))
    return render_template('signup.html',params=params)

@app.route('/run_egg', methods=['POST'])
def run_egg():
    # Execute your Python script here
    result = subprocess.run(['python', 'egg.py'], capture_output=True, text=True)
    print(result.stderr)
    return jsonify({'output': result.stdout})
@app.route('/run_snake', methods=['POST'])
def run_psnake():
    # Execute your Python script here
    result = subprocess.run(['python', 'snake.py'], capture_output=True, text=True)
    print(result.stderr)
    return jsonify({'output': result.stdout})
@app.route('/run_bird', methods=['POST','GET'])
def play_snake():
     return render_template('game1.html')
@app.route('/run_shoot', methods=['POST','GET'])
def play_shoot():
     return render_template('game2.html')
    


if __name__ == '__main__':
    app.run(port=5000) 

