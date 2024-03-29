#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'pablodecm'
SITENAME = u'pablodecm.com'
SITEURL = ''

PATH = 'content'

ARTICLE_PATHS = ['articles',]
PAGE_PATHS = ['pages',]

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

SITESUBTITLE=""

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

THEME=u'./theme'

HEADER_COLOR="black"
#BOOTSTRAP_THEME=u'readable'
AUTHORS_BIO = {
  "pablodecm": {
    "name" : "Pablo de Castro",
    "image" : "https://pbs.twimg.com/profile_images/1752319299111280640/8vIhffmJ_400x400.jpg",
    "website": "https://pablodecm.com",
    "twitter": "pablodecm",
    "github": "pablodecm",
    "bio": r"Data Scientist (Physics PhD) and Software Engineer<br>"
           r"Broadly interested in Machine Learning and Technology",
    "linkedin" : "pablodecm",
    "curriculum" : "pages/curriculum.html"
  }
}


CC_LICENSE='CC-BY-NC-SA'

STATIC_PATHS = ['extra', 'files']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicons/favicon.ico': {'path': 'favicon.ico'}}


PLUGIN_PATHS = ['./pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

AVATAR=None
ABOUT_ME=None
#DISPLAY_PAGES_ON_MENU =False
MENUITEMS = (('About','/index.html'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISQUS_SITENAME = "pablodecm"
GOOGLE_ANALYTICS = "UA-71094563-1"
