# -*- coding: utf-8 -*-

# pyminer

'''
pyminer library
~~~~~~~~~~~~~~~

pyminer is a Python client for text mining via Crossref metadata.

Usage::

    from pyminer import Miner
    m = Miner()
    m

    # search
    out = m.search(filter = {'has_full_text': True}, limit = 5)
    out.__class__

    # fetch
    from pyminer import fetch
    url = "http://www.banglajol.info/index.php/AJMBR/article/viewFile/25509/17126"
    out = fetch(url)
    out.url
    out.path
    out.type
    out.parse()

    # extract
	## pdf
	url = "http://www.banglajol.info/index.php/AJMBR/article/viewFile/25509/17126"
    out = fetch(url)
    out.parse()
'''

__version__ = '0.0.6.9000'
__title__ = 'pyminer'
__author__ = 'Scott Chamberlain'
__license__ = 'MIT'

from .miner import Miner
from .mined import Mined
from .fetch import fetch
from .extract import extract
from .links import links
from .parsers import parse_xml, parse_xml_string, parse_plain, parse_pdf
