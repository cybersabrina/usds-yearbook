import os

directory = os.path.dirname(os.path.realpath(__file__))

import sys
sys.path.append(os.path.join(directory, "MarkupSafe-1.0"))
sys.path.append(os.path.join(directory, "Jinja2-2.9.6"))
sys.path.append(os.path.join(directory, "web.py-0.38"))

import markupsafe
import jinja2
import web

