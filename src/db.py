from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import Config

session = None

def get_connection():
    global session
    
    if session is not None:
        return session
    try:
        config = Config()
        engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True)
        make_session = sessionmaker(bind=engine)
        session = make_session()
    except Exception as err:
        print("Cannot connect to database: {}".format(err))
    
    return session
        
