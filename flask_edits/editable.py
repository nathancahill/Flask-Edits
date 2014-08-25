"""Jinja extensions to mark sections as editable
"""

from collections import OrderedDict
import hashlib

from jinja2.nodes import Output, Template, TemplateData
from jinja2.ext import Extension


class EditableExtension(Extension):
    tags = set(['editable'])

    def parse(self, parser):
        _db = self.environment.edits

        # Skip begining node
        parser.stream.next()

        # Get section key
        key = parser.parse_expression().value

        # Read editable section
        section = parser.parse_statements(['name:endeditable'], drop_needle=True)

        # Render original section contents
        compiled = self.environment.compile(Template(section), '', '')
        original = self.environment.template_class.from_code(self.environment, compiled, {}, True).render()

        _db.setdefault(parser.name, OrderedDict())
        _db[parser.name].setdefault(key, OrderedDict())
        _db[parser.name][key].setdefault('original', original.strip())
        _db[parser.name][key].setdefault('edited', None)

        if _db[parser.name][key].get('edited', None):
            return Output([TemplateData(_db[parser.name][key]['edited'])])

        return section
