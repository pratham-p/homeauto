#!/usr/bin/env python3.4

#from flask import Flask, render_template
from flask import Blueprint, render_template

lightsapp = Blueprint(
        'lightsapp',
        __name__,
        template_folder='templates',
        static_folder='static',
        static_url_path='/app/static'
    )

#app = Flask(__name__)

@lightsapp.route('/')
def home():
    return render_template('home.html')

@lightsapp.route('/about/')
def about():
    return render_template('about.html')

#if __name__ == '__main__':
#    app.run(debug=True)