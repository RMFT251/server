from flask import Flask
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from flask"

@app.get("/test")
def test():
    return "This is another page"

# This will be the endpoints of the Json
# This is an API endpoint

@app.get("/api/about")
def about():
    me = {"name": "BigMeech"}
    return json.dumps(me)


app.run(debug=True)