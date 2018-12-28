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

        # search for many
        from pyminer import miner
        x = miner.search(filter = {'has_full_text': True}, limit = 5)
        x
        x.items
        x.links()
        x.links_verbose()
        x.links_unspecified()
        x.result
        x.fetch()

        # get by DOI
        from pyminer import miner
        x = miner.search(ids = '10.1371/journal.pone.0033693')
        x
        x.items
        x.items.keys()
        x.links()
        x.links_verbose()
        x.fetch()

        x = miner.search(ids = '10.3897/rio.2.e10445')
        x
        x.links()
        x.links_verbose()
        x.fetch()

        miner.search(filter = {
          'full_text_type': 'text/plain', 
          'license_url': "http://creativecommons.org/licenses/by-nc-nd/3.0"})
        miner.search(filter = {
          'has_full_text': True, 
          'license_url': "http://creativecommons.org/licenses/by/4.0"})
    '''
    cr = Crossref()
    if ids is not None:
        limit = None
    return Response(cr.works(ids = ids, limit = limit, filter = filter, **kwargs))
