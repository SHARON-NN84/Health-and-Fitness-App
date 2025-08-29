
from sqlalchemy import create_engine
from db.models.models import Base

def init_db():
    engine = create_engine('sqlite:///health_fitness.db')
    Base.metadata.create_all(engine)
    print("Database initialized successfully!")

if __name__ == '__main__':
    init_db()