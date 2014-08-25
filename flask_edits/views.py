"""Edits Admin Blueprint
"""

import os
import json

import jinja2

from flask import (
    Blueprint,
    current_app,
    render_template,
    request,
    redirect,
    url_for,
)

edits = Blueprint('edits', __name__, template_folder='templates', static_folder='static')

@edits.route('/', defaults={'page': None})
@edits.route('/<path:page>')
def index(page):
    _db = current_app.jinja_env.edits

    if _db:
        if not page:
            page = _db.iterkeys().next()
    else:
        page = None

    return render_template('edits-admin.j2', edits=_db, page=page, summernote=current_app.config['EDITS_SUMMERNOTE'])

@edits.route('/save', methods=['POST'])
def save():
    _db = current_app.jinja_env.edits

    page = request.form.get('page')

    for field in request.form:
        if field != 'page':
            value = request.form.get(field)

            if value == '':
                value = None

            _db[page][field]['edited'] = value

    current_app.jinja_env.cache.clear()

    with open(current_app.config['EDITS_PATH'], 'w') as f:
        f.write(json.dumps(_db, indent=4))

    return redirect(url_for('edits.index', page=page))
