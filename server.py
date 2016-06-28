#!/usr/bin/env python2

import subprocess
import tempfile

from flask import Flask, redirect, url_for
from flask_mako import MakoTemplates, render_template
from plim import preprocessor

app = Flask(__name__)
mako = MakoTemplates(app)
app.config['MAKO_PREPROCESSOR'] = preprocessor

def _chrome(url):
    subprocess.call([
        'google-chrome-stable', 
        '--user-data-dir=%s/flask-launcher' % tempfile.gettempdir(),
        '--kiosk', url
        ])

@app.route('/')
def index():
    return render_template('index.slim')

@app.route('/launch/netflix')
def netflix():
    _chrome('https://netflix.com')
    return redirect('/')

@app.route('/launch/youtube')
def youtube():
    _chrome('https://youtube.com/tv')
    return redirect('/')

@app.route('/launch/kodi')
def kodi():
    subprocess.call(['kodi'])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

