from flask import *
import sqlite3


app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def stud_reg():
    if request.method=='POST':
        n=request.form['fn']
        e=request.form['em']
        p=request.form['ph']
        with sqlite3.connect("login.db")as con:
            cur=con.cursor()
            cur.execute("""insert into student(name,mail,phone)values
                        (?,?,?)""",(n,e,p))
        return 'success'
    else:
        return render_template("studreg.html")
    


def stdView():
    con=sqlite3.connect("login.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from student")
    rows=cur.fetchall()

    return render_template("studreg.html",data=rows)
    

if __name__=="__main__":
    app.run(debug=True)