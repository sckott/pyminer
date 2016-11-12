from ..crutils import *
from ..response import Response
from habanero import Crossref

def search(ids=None, member=None, filter=None, limit=500, **kwargs):
    '''
    Search Crossref

    :param ids: [Array] DOIs (digital object identifier) or other identifiers
    :param member: [String] member ids
    :param filter: [Hash] Filter options. See ...
    :param limit: [Fixnum] Number of results to return. Not relavant when
        searching with specific dois. Default: 20. Max: 1000
    :param kwargs: any additional arguments will be passed on to
        `requests.get`

    :return: A dictionary, of results

    Usage::

        from pyminer import search
        search.search(ids = "10.1371/journal.pone.0000308")
        search.search(filter = {'has_full_text': True})
        search.search(filter = {'full_text_type': 'text/plain'})
    '''
    cr = Crossref()
    return Response(cr.works(ids = ids, limit = limit, filter = filter, **kwargs))
