# -*- coding: utf-8 -*-
#
from project import app
from flask import jsonify, abort, render_template, request, make_response
from ..utilities import Utility
from ..models import session, engine
from sqlalchemy import *
import json
import sys
import datetime
import pprint
import jwt

@app.route('/Security/isCookieValid', methods = ['POST'])
def isCookieValid():
	if 'ecoReleve-Core' in request.cookies:
		if 'securityKey' in request.json:
			decoded = jwt.decode(request.cookies['ecoReleve-Core'], verify=False)
			return (jsonify(decoded))
		else:
			abort(make_response('No security key given !', 400))
	else:
		abort(make_response('No reneco cookie given !', 400))