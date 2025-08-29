

# Import database building blocks from SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey, create_engine  # For creating tables and columns
from sqlalchemy.ext.declarative import declarative_base  # For creating our table classes
from sqlalchemy.orm import relationship, sessionmaker  # Connecting tables together
from datetime import datetime  # Handling dates and times

# This is the foundation for all table classes
Base = declarative_base()
engine = create_engine('sqlite:///health_fitness.db')
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# USER TABLE - Stores info about each person using the app
class User(Base):
    __tablename__ = 'users'  # Actual table name in database
    
    # COLUMNS
    id = Column(Integer, primary_key=True)  
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)  
    weight = Column(Float, nullable=False) 
    height = Column(Float, nullable=False) 
    created_at = Column(DateTime, default=datetime.now)  # When user was created (auto-filled)
    
    # RELATIONSHIPS
    nutrition_entries = relationship("Nutrition", back_populates="user", cascade="all, delete-orphan")
    exercise_sessions = relationship("Exercise", back_populates="user", cascade="all, delete-orphan")
    health_metrics = relationship("HealthMetric", back_populates="user", cascade="all, delete-orphan")
    
    # This makes user objects display well when printed
    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age}, weight={self.weight}, height={self.height})>"

# NUTRITION TABLE - Tracks what users eat
class Nutrition(Base):
    __tablename__ = 'nutrition'
    
    id = Column(Integer, primary_key=True)  
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  
    food = Column(String(200), nullable=False)  
    calories = Column(Float, nullable=False)  
    protein = Column(Float, default=0) 
    carbs = Column(Float, default=0)  
    fat = Column(Float, default=0)  
    timestamp = Column(DateTime, default=datetime.utcnow)  # When the food was logged (auto-filled)
    
    # RELATIONSHIP - Connect back to the user who owns this food entry
    user = relationship("User", back_populates="nutrition_entries")
    
    def __repr__(self):
        return f"<Nutrition(food='{self.food}', calories={self.calories}, timestamp={self.timestamp})>"

# EXERCISE TABLE - Tracks workout sessions
class Exercise(Base):
    __tablename__ = 'exercise'
    
    id = Column(Integer, primary_key=True)  
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  
    type = Column(String(100), nullable=False)  
    duration = Column(Integer, nullable=False)  
    calories_burned = Column(Float, nullable=False) 
    notes = Column(Text)  
    timestamp = Column(DateTime, default=datetime.utcnow) 
    
    # RELATIONSHIP - Connect back to the user
    user = relationship("User", back_populates="exercise_sessions")
    
    def __repr__(self):
        return f"<Exercise(type='{self.type}', duration={self.duration}, calories_burned={self.calories_burned})>"

# HEALTH METRICS TABLE - Tracks health measurements over time
class HealthMetric(Base):
    __tablename__ = 'health_metrics'
    
    id = Column(Integer, primary_key=True)  # Unique ID
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False) 
    weight = Column(Float) 
    blood_pressure = Column(String(20))  
    heart_rate = Column(Integer)  
    notes = Column(Text)  
    timestamp = Column(DateTime, default=datetime.utcnow)  
    
    # RELATIONSHIP - Connect back to the user
    user = relationship("User", back_populates="health_metrics")
    
    def __repr__(self):
        return f"<HealthMetric(weight={self.weight}, blood_pressure='{self.blood_pressure}', heart_rate={self.heart_rate})>"