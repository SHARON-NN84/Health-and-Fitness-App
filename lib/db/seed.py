# Import database building blocks from SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base  # For creating our table classes
from sqlalchemy.orm import relationship  # For connecting tables together
from datetime import datetime  # For handling dates and times

# This is the foundation for all our table classes
Base = declarative_base()ee