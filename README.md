Overview
A web application created in Python and Flask.

UX

Features
•	Create new recipes - recipe name, category, level of difficulty, servings, preparation time, method, ingredients.
•	Read recipes
•	Edit recipes
•	Delete recipes

Technologies Used
•	Bootstrap
o	CSS framework to style and create responsive design
•	Python
•	Flask
o	Python microframework
•	MongoDB
o	NoSQL database
•	Flask-Pymongo
o	Connects Flask to MongoDB

Testing

Deployment

Steps taken to deploy the website:
1.	Project workspace was created in GitPod.
2.	In this workspace: Flask was installed: 
CLI -> pip3 install flask
3.	Setup app.py file and imported flask and os: 
import os
from flask import Flask
4.	Created an instance of flask:
app = Flask(__name__)
5.	Inside the app run() function set the host, IP and debug=true
6.	Create a new Heroku App - unique name and EU Server
7.	In GitPod login to Heroku through CLI to confirm existance of app:
CLI: heroku login - CLI: heroku apps.
8.	Create a git repository in GitPod. CLI: git init. CLI: git add . CLI: git commit -m "Initial Commit"
9.	Connect GitPod to Heroku. Use code found on Heroku. CLI - $heroku git remote -a sagacity
10.	Create requirements.txt file:
CLI: pip3 freeze --local > requirements.txt
11.	Create Procfile:
echo web: python app.py > Procfile
12.	Add and commit to Git repository
13.	Push to Heroku using code supplied by Heroku
14.	Command to tell Heroku to run the app:
CLI - heroku ps:scale web=1 
15.	Login to Heroku to add config variables including IP, Port, Mongo_DB and Mongo_URI
16.	Get Flask to talk to MongoDB:
CLI: pip3 install flask-pymongo 
CLI: pip3 install dnspython
17.	Add extra libraries to app.py:
from flask_pymongo import Pymongo 
from bson.objectid import ObjectID
18.	Add DB connection code to app.py
19.	Test connection to DB to confirm it's working
20.	Connect GitHub repository to Heroku using code provided by Heroku and Github.
21.	Set debug to False


https://www.themealdb.com/api.php