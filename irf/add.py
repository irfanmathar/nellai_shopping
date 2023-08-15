from flask import flask,app,render_template,url_for,redirect,request,flash
import _sqlite3
con=sqlite3.connect("user.db")
@app.route(("/add"),methods=['get'])
def insert(name,email_id,password,address,phone):
    if request.method=='post':
        name=request.form['name']
        phone=request.form['phone']

        email_id=request.form['email_id']
        address=request.form['address']
        password=request.form['password']

        con=_sqlite3.connect.cursor()
        qry="insert into user(name,email_id,password,address,phone) values (?,?,?,?,?);"
        con.execute(qry,(name,email_id,password,address,phone))
        con.commit()
        con.close()
        return redirect(url_for("add.db"))
    return render_template("add.html")

    if (con):
        print ("<script> alert(data inset)</script>")
    else:
        print("file not exit")

