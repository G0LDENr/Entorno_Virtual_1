from models.User import User

def get_all_users():
    return [User.query.all()]
