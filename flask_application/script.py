from datetime import datetime

from flask import current_app

from flask_application import db
from flask.ext.script import Command
from flask.ext.security.confirmable import confirm_user


class ResetDB(Command):
    """Drops all tables and recreates them"""
    def run(self, **kwargs):
        db.drop_all()
        

class PopulateDB(Command):
    """Fills in predefined data to DB"""
    def run(self, **kwargs):
        self.create_roles()
        self.create_users()

    @staticmethod
    def create_roles():
        for role in ('admin', 'editor', 'author'):
            current_app.user_datastore.create_role(name=role, description=role)
        current_app.user_datastore.commit()

    @staticmethod
    def create_users():
        for u in (('matt', 'matt@lp.com', 'password', ['admin'], True),
                  ('joe', 'joe@lp.com', 'password', ['editor'], True),
                  ('jill', 'jill@lp.com', 'password', ['author'], True),
                  ('tiya', 'tiya@lp.com', 'password', [], False)):
            user = current_app.user_datastore.create_user(
                email=u[1],
                password=u[2],
                roles=u[3],
                active=u[4],
                confirmed_at = datetime.now()
            )
            confirm_user(user)

            current_app.user_datastore.commit()
