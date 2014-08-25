### Flask-Edits

"Can't you just, rewrite it to sound more _edgy?_"

Clients blowing up your phone to change some copy on the ```/about``` page?

Enter __Flask-Edits__. Mark sections of your templates as ```{% editable %}``` and their content is exposed in a slick admin panel. Never worry about tweaking copy again.

![Screenshot](http://i.imgur.com/XQYJbdQ.png)

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

Mark sections of your Jinja templates as editable.

```
{% editable %}
Python is a programming language that lets you work quickly and integrate systems more effectively.
{% endeditable %}
```

Visit the URL that renders the template to register the ```editable``` section. It will not show up in the admin panel if you don't load the page first.

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

Each editable section is stored using the hash of it's original content. Therefore, if you have multiple sections with the same content, it will only appear once in the admin panel, but changing it will change all sections.

Clearing a section will revert it to the original content in the template.

__Beware__

Changing an editable section in a template file changes it's hash. You'll have to re-register the section and add the edits again.

#### Roadmap

* Automatically register editable sections
* Jinja2 content with context evaluation
* Named sections
* Preview edits
* Multiple database backends
* In-place page editing
