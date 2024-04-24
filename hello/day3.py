from flask import *

app=Flask(__name__)



@app.route('/gtstud',methods=['GET'])
def mygetmthd():
    name=request.args.get("fn")
    email=request.args.get("em")
    phone=request.args.get("ph")
    print(name,email,phone)
    return 'success'


@app.route('/ptstud',methods=['POST'])
def mypostmthd():
    name=request.form['fn']
    email=request.form['em']
    phone=request.form['ph']
    print(name,email,phone)
    return 'success POST METHOD'


@app.route('/')
def getdata():
    if request.method="post"

    






if __name__=="__main__":
    app.run(debug=True)