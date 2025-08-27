# Import database building blocks from SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base  # For creating our table classes
from sqlalchemy.orm import relationship  # For connecting tables together
from datetime import datetime  # For handling dates and times

# This is the foundation for all our table classes
Base = declarative_base()
# USER TABLE - Stores information about each person using the app
class User(Base):
    __tablename__ = 'users'  # Actual table name in database
    
    # COLUMNS (like Excel spreadsheet columns)
    id = Column(Integer, primary_key=True)  # Unique ID for each user
    name = Column(String(100), nullable=False)  # User's name 
    age = Column(Integer, nullable=False)  # User's age (required)
    weight = Column(Float, nullable=False)  # User's weight (required)
    height = Column(Float, nullable=False)  # User's height (required)
    created_at = Column(DateTime, default=datetime.utcnow)  # When user was created
    
    # This makes user objects display nicely when printed
    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age}, weight={self.weight}, height={self.height})>"
# NUTRITION TABLE - Tracks what users eat
class Nutrition(Base):
    __tablename__ = 'nutrition'
    
    id = Column(Integer, primary_key=True)  # Unique ID for each food entry
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Which user this belongs to
    food = Column(String(200), nullable=False)  # What food was eatn
    calories = Column(Float, nullable=False)  # How many calores
    protein = Column(Float, default=0)  # Protein content (optional, defaults to 0)
    carbs = Column(Float, default=0)  # Carbohydrates content (optional)
    fat = Column(Float, default=0)  # Fat content (optional)
    timestamp = Column(DateTime, default=datetime.utcnow)  # When the food was logged 
    
    # RELATIONSHIP - Connect back to the user who owns this food entry
    user = relationship("User", back_populates="nutrition_entries")
    
    def __repr__(self):
        return f"<Nutrition(food='{self.food}', calories={self.calories}, timestamp={self.timestamp})>"