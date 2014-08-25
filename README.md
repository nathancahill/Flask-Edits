### Flask-Edits

"Can't you just, rewrite it to sound more _edgy?_"

Clients blowing up your phone to change some copy on the ```/about``` page?

Enter __Flask-Edits__. Mark sections of your templates with ```{% editable %}``` and their content is exposed in a slick admin panel. Never worry about tweaking copy again.

![Screenshot](http://i.imgur.com/7vCTJSN.png)

#### Usage

```
from flask.ext.edits import Edits

app = Flask(__name__)
edits = Edits(app)
```

All edits are saved to the disk as JSON, so configure a path to save the edits. Edits can be commited to version control along with the rest of the app.

```
import os.path as op
app.config['EDITS_PATH'] = op.join(op.dirname(op.abspath(__file__)), 'edits.json')
```

Mark sections of your Jinja templates as editable. The section name is required, it's used as the section label when editing and the key that the edits are stored under.

```
{% editable 'Section name' %}
Python is a programming language that lets you work quickly and integrate systems more effectively.
{% endeditable %}
```

__Important:__

There is no automatic detection of editable sections (yet). You have to visit the URL that renders the template to register it as editable. It will not show up in the admin panel until it has been rendered with ```render_template```.

#### Admin

The Flask-Edits admin view is exposed by default at ```/edits```. This can be changed in the configuration:

```
app.config['EDITS_URL'] = '/edits'
```

__Note on security:__

Like Flask-Admin, Flask-Edits does not make any assumptions about the authentication system you might be using. So, by default, the admin interface is completely open. Protect it behind basic auth or another form of authentication.

#### Editing

All pages that have registered editable sections are available to edit in the interface. At this time, only static HTML is supported. Support for Jinja2 is on the roadmap.

The [Summernote](http://hackerwins.github.io/summernote/) HTML editor is included but not used by default. To enable it:

```
app.config['EDITS_SUMMERNOTE'] = True
```

When content is saved it instantly updates the Jinja context and writes to the JSON file on the server.

Within a page, multiple sections with the same name will only show up once in the admin panel, but the edits will be applied to each section.

Clearing a section will revert it to the original content in the template.

#### Roadmap

* Automatically register editable sections
* Jinja2 content with context evaluation
* Preview edits
* Multiple database backends
* In-place page editing
