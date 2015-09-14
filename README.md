lazystrap
=========

Lazystrap is my very first Pelican theme. Theme based on Twitter Bootstrap. Theme are not using author(s) and category templates. Search based on ``tipue_search`` plugin.
Note, that for correct work, next variables must be set in ``pelicanconf.py`` exactly as in example:
- ``TAG_URL = 'tag/{slug}'``
- ``TAG_SAVE_AS = 'tag/{slug}/index.html'``
- ``ARTICLE_URL = 'blog/{slug}'``
- ``ARTICLE_SAVE_AS = 'blog/{slug}/index.html'``
- ``ARCHIVES_SAVE_AS = 'archives/index.html'``
- ``PAGINATED_DIRECT_TEMPLATES = ('archives',)``
- ``PAGINATION_PATTERNS = ((1, '{base_name}/', '{base_name}/index.html'), (2, '{base_name}/page{number}/', '{base_name}/page{number}/index.html'))``


Other theme variables:
- ``SITENAME = ""``
- ``SITESUBTITLE = ""``
- ``SITEKEYWORDS = ""``
- ``SITEURL = ""``
- ``SOCIAL = (('twitter', 'http://twitter.com/yourusername'),)``
- ``GITHUB_USERNAME = ""``

Screenshot
----------

![hello](screenshot.png)
