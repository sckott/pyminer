# -*- coding: utf-8 -*-

# pyminer

'''
pyminer library
~~~~~~~~~~~~~~~

pyminer is a Python client for text mining via Crossref metadata.

Usage::

		import pyminer
'''

__version__ = '0.0.1.9000'
__title__ = 'pyminer'
__author__ = 'Scott Chamberlain'
__license__ = 'MIT'

from .occurrences import search, get, count, download
from .species import names,name_parser
from .registry import datasets, nodes
from .gbifissues import occ_issues_lookup
