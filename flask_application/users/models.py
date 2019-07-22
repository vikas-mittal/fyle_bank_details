from flask.ext.security import UserMixin, RoleMixin
from flask_application import db
from flask.ext.security.utils import encrypt_password, verify_password
from datetime import datetime

roles_users = db.Table('roles_users', 
	db.Column('user_id', db.Integer(), db.ForeignKey('User.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('Role.id')))

class Role(db.Model, RoleMixin):
	__tablename__ = 'Role'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	description = db.Column(db.String(255))

class User(db.Model, UserMixin):
	__tablename__ = 'User'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(255), unique=True)
	password = db.Column(db.String(255))
	active = db.Column(db.Boolean())
	confirmed_at = db.Column(db.DateTime())
	roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    
	def __init__(self, email, password, active, confirmed_at=None, roles='client'):
		""" CLASS CONSTRUCTOR """
		self.email = email.lower()
		self.set_password(password)
		self.active = active
		self.confirmed_at = confirmed_at
		self.roles = roles
        
	def set_password(self, password):
		"""SET PASSWORD ENCRYPTED WITH CONFIG ALGO AND SALT VALUE"""
		self.password = encrypt_password(password)
   
	def check_password(self, password):
		"""CHECK PASSWORD FOR LOGIN AUTHENTICATION """
		return verify_password(password, self.password)