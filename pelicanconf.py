#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pablo de Castro'
SITENAME = u'pablodecm.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ((u'AMVA4NewPhysics', 'https://amva4newphysics.wordpress.com/'),
         (u'Tommaso Dorigo', 'http://www.science20.com/quantum_diaries_survivor'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/pablodecm'),
          ('github', 'http://github.com/pablodecm'),)


DEFAULT_PAGINATION = 10

THEME=u'./pelican-bootstrap3'
BOOTSTRAP_THEME=u'simplex'

CC_LICENSE='CC-BY-NC-SA'

STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}


PLUGIN_PATHS = ['./pelican-plugins', ]
#PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

