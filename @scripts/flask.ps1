cd ./server/
$env:FLASK_APP= "main.py"
$env:FLASK_ENV= "development" 
$env:FLASK_DEBUG= "1"
flask run