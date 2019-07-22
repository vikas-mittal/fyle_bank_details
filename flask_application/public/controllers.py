import datetime
import json
from flask import Blueprint, current_app, render_template
from flask.ext.security import login_required
from flask.ext.classy import FlaskView, route

from flask_application.controllers import TemplateView

public = Blueprint('public', __name__)


class IndexView(TemplateView):
    blueprint = public
    route = '/'
    route_name = 'home'
    template_name = 'home/index.html'

    def get_context_data(self, *args, **kwargs):
        return {
            'now': datetime.datetime.now(),
            'config': current_app.config
        }
        
class TestView(TemplateView):
    blueprint = public
    route='/test'
    route_name = 'test'
    #decorators=[login_required]
    
    def post(self):
        returnObj = json.dumps({'name': "Ajay", "age": 23, "languageKnown": ['C', 'C++', 'python']});
        return returnObj
    
