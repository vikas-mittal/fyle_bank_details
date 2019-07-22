from flask_application import app

import flask_restful as restful
from flask.ext.login import LoginManager, UserMixin, \
    login_required, login_user, logout_user
from flask import Flask, render_template, url_for, request, session, redirect, make_response
from flask_cors import CORS, cross_origin

CORS(app, supports_credentials=True)

api = restful.Api(app)



class GetToken(restful.Resource):
    @login_required
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("search/main.html"),200,headers)





api.add_resource(GetToken, '/get_token')