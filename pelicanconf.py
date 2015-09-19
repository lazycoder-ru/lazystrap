#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

ARCHIVES_SAVE_AS = 'archives/index.html'

PAGINATED_DIRECT_TEMPLATES = ('archives',)
PAGINATION_PATTERNS = ((1, '{base_name}/', '{base_name}/index.html'), (2, '{base_name}/page{number}/', '{base_name}/page{number}/index.html'))

BLOG_START_YEAR = "2008"

COMMENT_SYSTEM_ID = "20774"

ARCHIVES_TITLE = "Archives"
COMMENTS_TITLE = "Comments"
FEED_TITLE = "RSS"
RECENT_POSTS_TITLE = "Recent posts"
SEARCH_TITLE = "Search"
PREV_TITLE = "Prev"
NEXT_TITLE = "Next"
TAG_PAGE_TITLE = "Post tagged by"
