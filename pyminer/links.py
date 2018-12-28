from .miner import Miner

def links(ids, **kwargs):
    '''
    Get Crossref text mining links for specific DOIs

    :param ids: [Array] DOIs (digital object identifier) or other identifiers
    :param kwargs: any additional arguments will be passed on to
        ``requests.get``

    :return: A dictionary, of results

    Usage::

        from pyminer import links
        links(ids = '10.1371/journal.pone.0033693')
        links(ids = '10.3897/rio.2.e10445')
    '''
    m = Miner()
    res = m.search(ids = ids, **kwargs)
    res = res.links_verbose()
    return res
