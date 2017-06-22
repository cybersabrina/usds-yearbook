import os

from lib import jinja2
from lib import web

import directory

def load_template(template_path):
    directory, filename = os.path.split(template_path)
    directory = directory if directory else './templates'
    loader = jinja2.Environment(loader=jinja2.FileSystemLoader(directory))
    template = loader.get_template(filename)
    return template

def render_template(template, fields):
    return template.render(fields)


# This is where we map the URL paths to the handlers that will run when they're hit.
# One is given to you. You'll have to fill in the rest... :P
urls = (
    '/', 'Home'
)

class Home(object):
    def GET(self):
        template = load_template('get_home.html')
        return render_template(template, {})



if __name__ == '__main__':
    d = directory.TestDirectory()
    j = d.to_json()
    print j
    newd = directory.LocalDirectory.from_json(j)
    print newd
    app = web.application(urls, globals())
    app.run()
