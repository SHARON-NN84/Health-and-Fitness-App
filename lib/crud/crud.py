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

# NUTRITION CRUD OPERATIONS

def add_nutrition_entry(session: Session, user_id: int, food: str, calories: float, 
                       protein: float = 0, carbs: float = 0, fat: float = 0):
    """Add a food entry for a user"""
    nutrition = Nutrition(
        user_id=user_id,
        food=food,
        calories=calories,
        protein=protein,
        carbs=carbs,
        fat=fat
    )
    session.add(nutrition)
    session.commit()
    session.refresh(nutrition)
    return nutrition

def get_nutrition_entries(session: Session, user_id: int, date_str: str = None):
    """Get food entries for a user, optionally for a specific date"""
    query = session.query(Nutrition).filter(Nutrition.user_id == user_id)
    if date_str:
        try:
            target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            query = query.filter(
                Nutrition.timestamp >= datetime.combine(target_date, datetime.min.time()),
                Nutrition.timestamp <= datetime.combine(target_date, datetime.max.time())
            )
        except ValueError:
            pass
    return query.order_by(Nutrition.timestamp.desc()).all()

# EXERCISE CRUD OPERATIONS

def add_exercise_session(session: Session, user_id: int, type: str, duration: int, 
                        calories_burned: float, notes: str = None):
    """Add an exercise session for a user"""
    exercise = Exercise(
        user_id=user_id,
        type=type,
        duration=duration,
        calories_burned=calories_burned,
        notes=notes
    )
    session.add(exercise)
    session.commit()
    session.refresh(exercise)
    return exercise

def get_exercise_sessions(session: Session, user_id: int, date_str: str = None):
    """Get exercise sessions for a user, optionally for a specific date"""
    query = session.query(Exercise).filter(Exercise.user_id == user_id)
    if date_str:
        try:
            target_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            query = query.filter(
                Exercise.timestamp >= datetime.combine(target_date, datetime.min.time()),
                Exercise.timestamp <= datetime.combine(target_date, datetime.max.time())
            )
        except ValueError:
            pass
    return query.order_by(Exercise.timestamp.desc()).all()