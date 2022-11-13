from flask import Flask,render_template,request,redirect
import pymysql

app=Flask('__name__')

@app.route('/')
def index():
    try:
        db=pymysql.connect(host="localhost",user="root",password="sneha17@kum",database="hospitals")
        cu=db.cursor()
        q="select* from Flaska"
        cu.execute(q)
        data=cu.fetchall()
        return render_template("flask.html",d=data)
    except Exception as e:
        return("Error:")
    

@app.route('/create')
def create():
    return render_template("form.html")

@app.route('/store',methods=['POST'])
def store():
    n=request.form['n']
    d=request.form['d']
    dt=request.form['dt']
    #return t+"-"+det+"-"+dt
    try:
        db=pymysql.connect(host="localhost",user="root",password="sneha17@kum",database="hospitals")
        cu=db.cursor() #variable to hold cursor
        q="insert into flaska(Name,Detail,date) values('{}','{}','{}')".format(n,d,dt)
        cu.execute(q)  #executes the query with the help of cursor
        db.commit()
        return redirect('/')

    except Exception as e:
        return("Error:",+e)

@app.route('/delete/<rid>')
def delete(rid):
    try:
        db=pymysql.connect(host="localhost",user="root",password="sneha17@kum",database="hospitals")
        cu=db.cursor()
        q="delete from flaska where id='{}'".format(rid)
        cu.execute(q)
        db.commit()
        return redirect('/')
        
    except Exception as e:
        return("Error:")

@app.route('/edit/<rid>')
def edit(rid):
    try:
        db=pymysql.connect(host="localhost",user="root",password="sneha17@kum",database="hospitals")
        cu=db.cursor()
        q="select* from flaska where id='{}'".format(rid)
        cu.execute(q)
        data=cu.fetchone()
        return render_template('editform.html',d=data)
    
    except Exception as e:
        return("Error:")
    
@app.route('/update/<rid>',methods=['POST'])
def update(rid):
    un=request.form['n']
    ud=request.form['d']
    udt=request.form['dt']
    #return un+'-'+ud+'-'+udt
   
    try:
        db=pymysql.connect(host="localhost",user="root",password="sneha17@kum",database="hospitals")
        cu=db.cursor()
        q="update flaska SET name='{}',detail='{}',date='{}' where Id='{}'".format(un,ud,udt,rid)
        cu.execute(q)
        db.commit()
        return redirect('/')
    except Exception as e:
        return("Error:")
    

app.run(debug=True)