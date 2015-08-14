from jinja2 import Markup
from jinja2 import escape

def newlinetobr(value):
    return Markup('<br />'.join(escape(value).splitlines()))