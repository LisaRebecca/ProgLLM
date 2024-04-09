from flask import Flask, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Database connection details
DB_HOST = "db"
DB_NAME = "mydatabase"
DB_USER = "myuser"
DB_PASS = "mypassword"

def get_db_connection():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    return conn

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['user_id']
        except:
            return jsonify({'message': 'Token is invalid!'}), 403

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/login_status', methods=['GET'])
@token_required
def login_status(current_user):
    return jsonify({'message': f'User {current_user} is currently logged in.'})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = generate_password_hash(data['password'])

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()

    cur.close()
    conn.close()

    return jsonify({'message': 'Registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()

    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("SELECT * FROM users WHERE username = %s", (auth['username'],))
    user = cur.fetchone()

    cur.close()
    conn.close()

    if not user or not check_password_hash(user['password'], auth['password']):
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    token = jwt.encode({
        'user_id': user['id'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }, app.config['SECRET_KEY'])

    return jsonify({'token': token})

@app.route('/protected', methods=['GET'])
@token_required
def protected(current_user):
    return jsonify({'message': f'Welcome user {current_user}'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5420)
