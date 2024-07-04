from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 

class Comment:
    def __init__(self, data):
        self.id = data['id']
        self.post_id = data['post_id']
        self.user_id = data['user_id']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.user_name = data['user_name']

    @classmethod
    def save_comment(cls, form):
        query = 'insert into comments (post_id, user_id, comment) values (%(post_id)s, %(user_id)s, %(comment)s);'
        return connectToMySQL('foro_publicaciones').query_db(query, form)
    
    @staticmethod
    def validate_comment(form):
        is_valid = True
        if len(form['comment']) < 1:
            flash('Comentario inválido, agrege caracteres para comentar :)', 'comment')
            is_valid = False
        return is_valid
    
    @classmethod
    def view_comment_post(cls, data):
        query = 'select comments.*, users.first_name as user_name from comments join users on comments.user_id = users.id where comments.post_id = %(id)s order by created_at desc;'
        result = connectToMySQL('foro_publicaciones').query_db(query, data)

        comments = []
        for comment in result:
            comments.append(cls(comment))
        return comments
    
    