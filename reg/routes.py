
from flask import Flask, render_template, request

from reg import app,db

from reg.models import *





@app.route('/',methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        email = request.form['email']
        contact = request.form['contact']
        password = request.form['password']
        my_data = Register(name=name, address=address,email=email,contact=contact,password=password)
        db.session.add(my_data) 
        db.session.commit()
        d="Registered Successfully"
        return render_template('register.html',d=d)
        
    else :
        return render_template("register.html")



