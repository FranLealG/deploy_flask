from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
from flask_app.models.comment import Comment

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        self.user_name = data['user_name']
        self.comment = data['comment']

    @classmethod
    def save(cls, form):
        query = 'insert into posts (content, user_id) values (%(content)s, %(user_id)s);'
        return connectToMySQL('foro_publicaciones').query_db(query, form)
    
    @staticmethod
    def validate_post(form):
        is_valid = True
        if len(form['content'])<1:
            flash('El contenido no es válido', 'post')
            is_valid = False
        return is_valid
    
    @classmethod
    def get_all(cls):
        query = 'select posts.*, users.first_name as user_name from posts join users on posts.user_id = users.id order by posts.created_at desc;'
        results = connectToMySQL('foro_publicaciones').query_db(query) 
        # [{},{},{},{}] -> {} -> id - content -creat - updat - user id - nombre_usuario - *list_comment* 
        
        posts = []
        for post in results:
            dicc = {'id': post['id']}
            comentarios = Comment.view_comment_post(dicc)
            post['comment'] = comentarios
            posts.append(cls(post))
        return posts
    
    @classmethod
    def delete(cls, data):
        query = 'delete from posts where id = %(id)s;'
        return connectToMySQL('foro_publicaciones').query_db(query, data)