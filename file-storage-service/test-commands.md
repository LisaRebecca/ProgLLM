curl -X POST http://localhost:34568/upload \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MTI2NTk4NjF9.9OtyPMf8rkh7m9bnL4SiBep_Tl-tPZcXwHTIm8YTWGk" \
  -F "folder=myfolder" \
  -F "file=@test_files/orca.txt" 


curl -X GET http://localhost:34568/list?folder=myfolder \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE3MTI2NTkxNzB9.qZbA4idLqfXf4cSCcvvhfhhyMIom860KB8MOjCnY2DE"

curl -X GET "http://localhost:34568/read/myfolder/orca.txt"

curl -X GET http://localhost:34568/download/myfolder/orca.txt --output orca.txt

curl -X DELETE http://localhost:34568/delete/myfolder/orca.txt
