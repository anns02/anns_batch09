from flask import*
 app = Flask(__name__)
app.secret_key="aaa"

@app.route("/nsss",method=['POST','GET'])
def get_session():
 if request.method=="POST":
  name=request.form["fname"]
  email=request.form["em"]
  password=request.forms["pass"]
  if password=="admin":
    session