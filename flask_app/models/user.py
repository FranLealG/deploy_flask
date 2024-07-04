from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash #flash es el encargado de mostrar los mensajes

import re #Expresiones Regulares | mach con un patron de texto
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Expresion regular de email

class User:
    def __init__(self, data):
        #data :{diccionario con toda la info de la instancia}
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #metodo para un nuevo registro
    @classmethod
    def save(cls, form):
        #form: {'first_name': 'nombre', etc ... 'password' = YA_HASHEADA}
        query = 'insert into users (first_name, last_name, email, password) values (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'
        return connectToMySQL('foro_publicaciones').query_db(query, form)
    
    #metodo para saber si existe un usuario
    @classmethod
    def get_by_email(cls, form):
        query = 'select * from users where email = %(email)s;'
        result = connectToMySQL('foro_publicaciones').query_db(query, form) #retorna una lista de diccionarios 
        if len(result) < 1: #revisa que la lista esté vacía
            return False
        else: #retorna un registro
            return cls(result[0])
        
    #metodo de clase para recibir el nombre del usuario
    @classmethod
    def get_by_name(cls, form):
        query = 'select * from users where id = %(id)s;'
        result = connectToMySQL('foro_publicaciones').query_db(query, form)
        return cls(result[0])
        
    #metodo que valide la info recibida del formulario 
    @staticmethod
    def validate_user(form):
        is_valid =  True 

        #validamos que el nombre tenga al menos 2 caracteres
        if len(form['first_name']) < 2:
            flash('Tu nombre debe tener al menos 2 caracteres', 'register') #flash(mensaje, categoria)
            is_valid =  False
        
        if len(form['last_name']) < 2:
            flash('Tu apellido debe tener al menos 2 caracteres', 'register')
            is_valid =  False

        if len(form['password']) < 6:
            flash('Tu contraseña debe tener al menos 6 caracteres', 'register')
            is_valid =  False
        
        #validar que el correo sea único
        query = 'select * from users where email = %(email)s;'
        result = connectToMySQL('foro_publicaciones').query_db(query, form)

        if len(result) >= 1:
            flash('El email ya estaba registrado', 'register')
            is_valid = False

        #validar que las pass sean iguales
        if form['password'] != form['confirm-pass']:
            flash('Las constraseñas no son iguales!', 'register')
            is_valid = False

        #validar que el email sea valido
        if not EMAIL_REGEX.match(form['email']): #mach compara una expresion regular con un texto
            flash('El email no es válido', 'register')
            is_valid = False

        return is_valid