from app.ticket_notifier import db
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
