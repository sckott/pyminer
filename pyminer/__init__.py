# -*- coding: utf-8 -*-

# pyminer

'''
pyminer library
~~~~~~~~~~~~~~~

pyminer is a Python client for text mining via Crossref metadata.

Usage::

    import pyminer

    # search
    pyminer.search(filter = {'has_full_text': True}, limit = 5)

    # fetch
    url = "http://www.banglajol.info/index.php/AJMBR/article/viewFile/25509/17126"
    out = pyminer.fetch(url)
    out.url
    out.path
    out.type
    out.parse()

    # extract
		## pdf
		url = "http://www.banglajol.info/index.php/AJMBR/article/viewFile/25509/17126"
    out = pyminer.fetch(url)
    out.parse()
'''

__version__ = '0.0.5.9000'
__title__ = 'pyminer'
__author__ = 'Scott Chamberlain'
__license__ = 'MIT'

from .miner import search, fetch, extract, links
from .parsers import parse_xml, parse_xml_string, parse_plain, parse_pdf
