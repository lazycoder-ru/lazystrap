#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'lazycoder'
SITENAME = u'lazystrap'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

THEME = "themes/lazystrap"

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

ARCHIVES_SAVE_AS = 'archives/index.html'

PAGINATED_DIRECT_TEMPLATES = ('archives',)
PAGINATION_PATTERNS = ((1, '{base_name}/', '{base_name}/index.html'), (2, '{base_name}/page{number}/', '{base_name}/page{number}/index.html'))
