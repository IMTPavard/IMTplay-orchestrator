from flask import Flask
app = Flask(__name__)

# gogol alert : use git push --tags

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There! It's orchestrator v6</h1>"