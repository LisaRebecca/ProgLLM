curl -X POST http://localhost:34568/upload \
  -F "folder=myfolder" \
  -F "file=@test_files/orca.txt"

curl -X GET "http://localhost:34568/list?folder=myfolder"

curl -X GET "http://localhost:34568/read/myfolder/orca.txt"

curl -X GET http://localhost:34568/download/myfolder/orca.txt --output orca.txt

curl -X DELETE http://localhost:34568/delete/myfolder/orca.txt
