from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app import app

#importar bcrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/register', methods=['post'])
def register():
    #request.form = {'first_name': 'nombre', etc}
    #validar la info que se recibe
    if not User.validate_user(request.form):
        return redirect("/")
    
    #hashear la pass
    pass_hash = bcrypt.generate_password_hash(request.form['password'])

    #crear un diccionario que simule el form, incluyendo la contraseña hasheada
    form = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pass_hash
    }

    id = User.save(form) #recibo el id del nuevo usuario
    session['user_id'] = id #guardamos en session el id del usuario
    return redirect("/dashboard")

@app.route('/dashboard')
def dashboard():
    #verificar que el user haya iniciado sesion
    if 'user_id' not in session:
        return redirect("/")
    
    dicc = {"id": session["user_id"]}
    user = User.get_by_name(dicc)
    #enviar publicaciones
    posts = Post.get_all()

    return render_template("dashboard.html", user = user, posts=posts)

@app.route("/login", methods=['post'])
def login():
    #request.form = {'email': 'aaa@', 'pass': 'aaa'}
    #verifico que el emmail esté en la bd
    user = User.get_by_email(request.form) #recibe false o un objeto de usuario

    if not user:
        flash('Email no existe', 'login')
        return redirect("/")
    
    if not bcrypt.check_password_hash(user.password, request.form['password']): #(pass hasheado, pass no hasheado)
        flash('Contraseña incorrecta', 'login')
        return redirect("/")
    
    session['user_id'] = user.id
    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")