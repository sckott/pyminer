from .search import search

def links(ids, **kwargs):
    '''
    Get Crossref text mining links for specific DOIs

    :param ids: [Array] DOIs (digital object identifier) or other identifiers
    :param kwargs: any additional arguments will be passed on to
        ``requests.get``

    :return: A dictionary, of results

    Usage::

        from pyminer import miner
        x = miner.links(ids = '10.1371/journal.pone.0033693')
        x

        x = miner.links(ids = '10.3897/rio.2.e10445')
        x
    '''
    res = search(ids = ids, **kwargs)
    res = res.links_verbose()
    return res
