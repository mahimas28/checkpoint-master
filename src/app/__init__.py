# -*- coding: utf-8 -*-

import jinja2
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from flask import Flask
from datetime import datetime


# to avoid request warning of using verify=false
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

app = Flask(__name__)
# config file for development
app.config.from_object('config')

# config file por production
# app.instance_path = os.path.abspath(os.path.join(os.path.dirname(__file__), \
# 	'..'))
# config_file_path = app.instance_path + '/instance/config.py'
# app.config.from_pyfile(config_file_path)

from . import views  #from app import views
from . import api_response
from . import cp_mgmt_api
from . import forms
from . import models
from . import run

def datetimeformat(value, format='%d/%m/%Y %H:%M'):
    return datetime.fromtimestamp(int(value) / 1000).strftime(format)


jinja2.filters.FILTERS['datetimeformat'] = datetimeformat
