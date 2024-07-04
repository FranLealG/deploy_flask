#pipenv install flask pymysql flask-bcrypts
#importación de la app| importar controladores (puede ser más de uno) | ejecución de app
from flask_app import app
from flask_app.controllers import user_controller, post_controller, comment_controller

if __name__ == '__main__':
    app.run(debug=True)