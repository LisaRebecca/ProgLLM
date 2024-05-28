
# Endpoint for authentication
AUTH_ENDPOINT="http://localhost:5420/login"

# Your user credentials
USERNAME="newuser"
PASSWORD="newpassword"

# Endpoint for file upload
UPLOAD_ENDPOINT="http://localhost:34568/upload"
FOLDER="myfolder"
FILE_PATH="test_files/orca.txt"

# Obtain Bearer Token
# Replace 'username' and 'password' with your actual login credentials' field names
TOKEN=$(curl -s -X POST "$AUTH_ENDPOINT" \
     -H "Content-Type: application/json" \
     -d "{\"username\":\"$USERNAME\", \"password\":\"$PASSWORD\"}" | jq -r '.token')

# Check if we got a token
if [ "$TOKEN" == "null" ] || [ -z "$TOKEN" ]; then
  echo "Failed to obtain token."
  exit 1
fi

echo "Obtained Token: $TOKEN"

# Use the token to upload a file
curl -X POST "$UPLOAD_ENDPOINT" \
     -H "Authorization: Bearer $TOKEN" \
     -F "folder=$FOLDER" \
     -F "file=@$FILE_PATH"

