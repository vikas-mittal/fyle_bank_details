from app import db_operations as db_ops
import bookings
import destiinations
import packages

from . import BASE

def create_all_tables():
    engine = db_ops.get_engine()
    BASE.metadata.create_all(engine, checkfirst=True)

if __name__=='__main__':
	create_all_tables()