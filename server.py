#!/usr/bin/env python2

import subprocess
import tempfile
import json

from flask import Flask, redirect, url_for
from flask_mako import MakoTemplates, render_template
from plim import preprocessor

app = Flask(__name__)
mako = MakoTemplates(app)
app.config['MAKO_PREPROCESSOR'] = preprocessor

with open('config.json') as f:
    launcher_config = json.loads(f.read())

def _chrome(url):
    subprocess.call([
        'google-chrome-stable', 
        '--user-data-dir=%s/flask-launcher' % tempfile.gettempdir(),
        '--kiosk', url
        ])

@app.route('/')
def index():
    return render_template('index.slim', launcher_config=launcher_config)

@app.route('/launch/<name>')
def launch(name):
    for n in launcher_config['launchers']:
        if n['name'] == name:
            if 'url' in n:
                _chrome(n['url'])
            elif 'cmd' in n:
                subprocess.call([n['cmd']])

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

