import jwt
from datetime import datetime, timedelta

def create_jwt_token(user_id):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': user_id
    }
    return jwt.encode(
        payload, 
        'your_secret_key', 
        algorithm='HS256'
    )
