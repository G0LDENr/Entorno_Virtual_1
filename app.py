from flask import Flask
from config import db,migrate
from routes.user import user_bp


app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'aqlite://app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app,db)

app.app.register_blueprint(user_bp,url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)