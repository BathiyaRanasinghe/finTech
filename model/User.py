from flask_login import UserMixin
from database.UserDB import user_db

MAX_EMAIL_LEN = 150
MAX_PASSWORD_LEN = 150
MAX_FIRST_NAME_LEN = 150


class User(user_db.Model, UserMixin):
    """
    A user account of the website
    """

    id = user_db.Column(user_db.Integer, primary_key=True)
    email = user_db.Column(user_db.String(MAX_EMAIL_LEN), unique=True)
    password = user_db.Column(user_db.String(MAX_PASSWORD_LEN))
    first_name = user_db.Column(user_db.String(MAX_FIRST_NAME_LEN))
