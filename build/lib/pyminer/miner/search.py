from ..crutils import *
from ..response import Response
from habanero import Crossref

def search(ids=None, member=None, filter=None, limit=500, **kwargs):
    '''
    Search Crossref to get text mining links

    :param ids: [Array] DOIs (digital object identifier) or other identifiers
    :param member: [String] member ids
    :param filter: [Hash] Filter options. See ...
    :param limit: [Fixnum] Number of results to return. Not relavant when
        searching with specific dois. Default: 20. Max: 1000
    :param kwargs: any additional arguments will be passed on to
        ``requests.get``

    :return: A dictionary, of results

    Usage::

        import pyminer
        pyminer.search(filter = {'has_full_text': True}, limit = 5)
        pyminer.search(filter = {'full_text_type': 'text/plain', 'license_url': "http://creativecommons.org/licenses/by-nc-nd/3.0"})
        pyminer.search(filter = {'has_full_text': True, 'license_url': "http://creativecommons.org/licenses/by/4.0"})
    '''
    cr = Crossref()
    return Response(cr.works(ids = ids, limit = limit, filter = filter, **kwargs))
