curl -X POST http://127.0.0.1:5420/register \
     -H "Content-Type: application/json" \
     -d '{"username":"newuser", "password":"newpassword"}'

curl -X POST http://localhost:5420/login \
     -H "Content-Type: application/json" \
     -d '{"username":"newuser", "password":"newpassword"}'

curl -X GET http://localhost:5420/login_status \
     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MTI2NTUyMzV9.apy9T6zr4mKZHTNUW__rHOE6MXOYioAbZ2mGfysLYfw"

TOKEN=$(curl -s -X POST http://localhost:5420/login \
     -H "Content-Type: application/json" \
     -d '{"username":"newuser", "password":"newpassword"}' | jq -r '.token')

echo "Obtained Token: $TOKEN"

curl -X GET http://localhost:5420/protected \
     -H "Authorization: Bearer $TOKEN"


psql -h localhost -U myuser -d mydatabase
SELECT * FROM USERS;