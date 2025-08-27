# Import necessary modules
from sqlalchemy.orm import Session
from datetime import datetime, date

# Import our database table models (like blueprints for our data)
from db.models.models import User, Nutrition, Exercise, HealthMetric

# USER CRUD OPERATIONS (Create, Read, Update, Delete)

def create_user(session: Session, name: str, age: int, weight: float, height: float):
    """Create a new user and save to database"""
    user = User(name=name, age=age, weight=weight, height=height)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_user(session: Session, user_id: int):
    """Find and return a specific user by their ID"""
    return session.query(User).filter(User.id == user_id).first()

def get_all_users(session: Session):
    """Get all users from the database"""
    return session.query(User).all()

def update_user(session: Session, user_id: int, **kwargs):
    """Update user information - you can pass any user attributes to change"""
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        session.commit()
        session.refresh(user)
    return user

def delete_user(session: Session, user_id: int):
    """Delete a user from the database"""
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return True
    return False