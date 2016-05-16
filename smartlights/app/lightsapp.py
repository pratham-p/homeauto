#!/usr/bin/env python3.4

#from flask import Flask, render_template
from flask import Blueprint, render_template
from smartlights.api.lightsapi import LightList
import requests

lights = Blueprint(
        'lights',
        __name__,
        template_folder='templates',
        static_folder='static',
        static_url_path='/app/static'
    )

#app = Flask(__name__)

@lights.route('/')
@lights.route('/home')
def home():
	lightsRequest = LightList()
	response, code = lightsRequest.get()
	if code == requests.codes.ok:
		return render_template('home.html', lightsList = response['lights'])
	else:
		return render_template('home.html')

@lights.route('/about/')
def about():
    return render_template('about.html')

#if __name__ == '__main__':
#    app.run(debug=True)
