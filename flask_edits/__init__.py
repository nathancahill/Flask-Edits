"""Flask-Edits
"""

from flask import request
from jinja2.environment import copy_cache

from collections import OrderedDict
import json
import os

from .editable import EditableExtension
from .views import edits


class Edits(object):
    def __init__(self, app=None):
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
            Register the Jinja extension, load edits from 
            app.config['EDITS_PATH'] and register blueprints.

            :param app:
                Flask application instance
        """
        app.config.setdefault('EDITS_URL', '/edits')
        app.config.setdefault('EDITS_PREVIEW', True)
        app.config.setdefault('EDITS_SUMMERNOTE', False)

        if 'EDITS_PATH' not in app.config:
            raise Exception('EDITS_PATH not set in app configuration.')

        if os.path.isfile(app.config['EDITS_PATH']):
            with open(app.config['EDITS_PATH']) as f:
                _db = json.loads(f.read(), object_pairs_hook=OrderedDict)
        else:
            _db = OrderedDict()

        app.jinja_env.add_extension('flask.ext.edits.EditableExtension')
        app.jinja_env.edits = _db
        app.jinja_env.edits_preview = app.config['EDITS_PREVIEW']
        app.jinja_env.edits_cache = copy_cache(app.jinja_env.cache)

        if app.config['EDITS_PREVIEW']:
            app.jinja_env.cache = None

        app.register_blueprint(edits, url_prefix=app.config['EDITS_URL'])
