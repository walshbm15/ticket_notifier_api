from app.ticket_notifier import db
from sqlalchemy import or_
from datetime import datetime, timedelta
from flask import current_app


class User(db.Model):
    """This class defines the users table """

    __tablename__ = 'users'

    # Define the columns of the users table, starting with the primary key
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=True)
    email = db.Column(db.String(256), nullable=True, unique=True)
    mobile = db.Column(db.String(256), nullable=True, unique=True)

    def __init__(self, name, email, mobile):
        """Initialize the user with an email and a password."""
        self.name = name
        self.email = email
        self.mobile = mobile

    def save(self):
        """Save a user to the database.
        This includes creating a new user and editing one.
        """
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_user(contact):
        """Return user info from database
        based on an email or phone number
        """
        user = User.query.filter(or_(User.email == contact, User.mobile == contact))

        return user
