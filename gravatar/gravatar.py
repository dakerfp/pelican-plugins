"""
Gravatar plugin for Pelican
===========================

This plugin assigns the ``author_gravatar`` variable to the Gravatar URL and
makes the variable available within the article's context.
"""

import hashlib
import json
import six
import urllib2

from pelican import signals


def add_gravatar(generator, metadata):

    #first check email
    if 'email' not in metadata.keys()\
        and 'AUTHOR_EMAIL' in generator.settings.keys():
            metadata['email'] = generator.settings['AUTHOR_EMAIL']

    #then add gravatar url and about
    if 'email' in metadata.keys():
        gravatar_url = "http://en.gravatar.com/" + metadata['email'] + ".json"
        data = json.load(urllib2.urlopen(gravatar_url))
        metadata['author_gravatar'] = data['entry'][0]['thumbnailUrl']
        if 'about_author' not in metadata.keys():
            metadata['about_author'] = data['entry'][0]['aboutMe']


def register():
    signals.article_generator_context.connect(add_gravatar)
