#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Georgi Zhelyazkov'
SITENAME = 'SINISTER SOUNDWORKS'
SITEURL = ''
SITESUBTITLE = 'Recording | Mixing | Mastering'

PATH = 'content'

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/jalapenogeorge'),
          ('Instagram', 'https://www.instagram.com/sinistersoundworks/'),
          ('Muso.ai', 'https://credits.muso.ai/profile/a386bf56-3fbb-4d43-92dc-064d13118dcf'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Markdown extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Jinja2 extensions
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Custom Jinja2 filters
def markdown_filter(text):
    import markdown
    return markdown.markdown(text)

JINJA_FILTERS = {'markdown': markdown_filter}

# Theme settings
THEME = 'themes/sinister'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Static paths - copy entire assets directory and CNAME
STATIC_PATHS = ['assets', 'extra/robots.txt', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
}

# Article settings
ARTICLE_URL = 'portfolio/{slug}/'
ARTICLE_SAVE_AS = 'portfolio/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Sort articles by filename number prefix (descending)
DEFAULT_PAGINATION = False

def article_sort_key(article):
    # Extract number from filename (e.g., "01-title" -> 1)
    import re
    match = re.match(r'(\d+)', article.source_path.split('/')[-1])
    return int(match.group(1)) if match else 0

ARTICLE_ORDER_BY = article_sort_key
REVERSE_ARTICLE_ORDER = True

# Custom variables for site content
SITE_DESCRIPTION = 'Recording | Mixing | Mastering'
HEADER_TITLE = "Hardcore & Metal Recordings that bite"
HEADER_TEXT = "Mixing • Mastering • Music Production"
HEADER_BUTTON = "Learn more"
HEADER_BUTTONLINK = "#services"
MASCOT_IMAGE = "assets/img/kitty.png"
FORMSPREE_FORM_PATH = 'f/xaykzoor'

# Analytics (production only)
ANALYTICS_DOMAIN = 'sinistersoundworks.com'
ANALYTICS_URL = 'https://analytics.sinistersoundworks.com/js/script.js'

# Services data
SERVICES = [
    {
        'title': 'Recording',
        'icon': 'lni lni-microphone',
        'description': '''A good mix begins with a good recording.  
I take every step to help you get it right from the very start.

I work with various studios, depending on the project requirements and budget.

Mobile recording on location and remote recording available as well.'''
    },
    {
        'title': 'Mixing',
        'icon': 'lni lni-headphone',
        'description': '''Whether you are after a crystal-clear sound or a dirty old-school vibe, I can take your recording from rough demo to release-ready mixes. 
My aim is to help you achieve your vision of your music, while making sure it sounds spot on.

If you'd prefer to master the song elsewhere, I will provide you with an unmastered version as well.

I can also provide stems at additional cost.'''
    },
    {
        'title': 'Mastering',
        'icon': 'lni lni-music',
        'description': '''Mastering for a single song or an album/EP.

Master for CD and streaming (44.1 kHz/16 bit)

High definition master (48 kHz/24 bit)

2 free revisions

Master for Vinyl

DDP Master (Albums/EPs only) included in the price.

Additional formats (radio edit, instrumentals etc.) available at extra cost.'''
    }
]

# About section
ABOUT_TITLE = 'About Me'
ABOUT_IMAGE = 'assets/img/about.png'
ABOUT_TEXT = '''Hello, I'm Georgi, a freelance audio engineer and full stack producer based in Prague, Czech Republic. I specialize in heavy-hitting genres like metal, hardcore, punk, and all things heavy rock, but I'm always eager to explore new music genres.

If you're looking for a creative partner to help you craft your next musical masterpiece, look no further. Get in touch and let's work together.'''

# Contact section
CONTACT_TITLE = 'Contact'
CONTACT_TEXT = "Let's talk about your project"
