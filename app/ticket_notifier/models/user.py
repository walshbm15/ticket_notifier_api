from app.ticket_notifier import db
from sqlalchemy import or_


class User(db.Model):
    """This class defines the users table """

    __tablename__ = 'users'

    # Define the columns of the users table, starting with the primary key
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=True)
    email = db.Column(db.String(256), nullable=True, unique=True)
    mobile = db.Column(db.String(256), nullable=True, unique=True)
    time_added = db.Column(db.DateTime, server_default=db.func.now())

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

    def delete(self):
        """Delete user from the database"""
        db.session.delete(self)
        db.session.commit()

    def get_user_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'mobile': self.mobile,
            'time_added': str(self.time),
        }

    @staticmethod
    def get_user(contact):
        """Return user info from database
        based on an email or phone number
        """
        user = User.query.filter(or_(User.email == contact, User.mobile == contact))
        if not user:
            return None

        return user
