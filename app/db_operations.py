"""
This modules helps in operations related to database. Connecting, querying, updating,
inserting etc. All the database operations are performed in this module.
"""

import json

from sqlalchemy import create_engine




def get_connection_string():
    """
    Creates a connection string for postgres database.
    :return: returns a connection string if successfully created.
    """
    # connection_string = 'postgresql://' + config.DB_USER + ":" + config.DB_PASSWORD + "@" \
    #                     + config.DB_HOST + ":" + config.DB_PORT + "/" + config.DB_NAME

    connection_string = "postgres://postgres:password@127.0.0.1:5432/postgres"
    return connection_string


def get_engine():
    """
    :return: Engine object based on get_connection_string() function which returns a
    connection string URL.
    """
    return create_engine(get_connection_string(), isolation_level="AUTOCOMMIT")


def connect_to_db():
    """
    Connect the database and creates a session.
    Session establishes all conversations with the database
    and represents a 'holding zone' for all the objects
    which you have loaded or associated with it
    during its lifespan.
    :return: Session
    """
    # This import is here to prevent circular import error from 'flask_application' package.
    from flask_application import session_maker
    session = session_maker()
    session.begin()
    return session

