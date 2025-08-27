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
    id = Column(Integer, primary_key=True)  # Unique ID for each user (auto-numbered)
    name = Column(String(100), nullable=False)  # User's name (required, max 100 chars)
    age = Column(Integer, nullable=False)  # User's age (required)
    weight = Column(Float, nullable=False)  # User's weight (required)
    height = Column(Float, nullable=False)  # User's height (required)
    created_at = Column(DateTime, default=datetime.utcnow)  # When user was created (auto-filled)
    
    # This makes user objects display nicely when printed
    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age}, weight={self.weight}, height={self.height})>"