import jwt

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MTI2NTk4NjF9.9OtyPMf8rkh7m9bnL4SiBep_Tl-tPZcXwHTIm8YTWGk'
secret_key = 'your_secret_key_here'

try:
    decoded = jwt.decode(token, secret_key, algorithms=["HS256"])
    print("Token is valid:", decoded)
except jwt.exceptions.ExpiredSignatureError:
    print("Token has expired")
except jwt.exceptions.InvalidTokenError:
    print("Token is invalid")