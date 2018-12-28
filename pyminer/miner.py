from .crutils import *
from .mined import Mined
from habanero import Crossref

class Miner(object):
  '''
  Miner: Class for mining Crossref articles
  
  |
  |

  **Miner Methods**

  * search - :func:`~pyminer.Miner.search`

  **Setup**::

    from pyminer import Miner
    m = Miner()
    # set a mailto address
    Miner(mailto = "foo@bar.com")
    # set your Crossref TDM key
    Miner(tdmkey = "123456")

  **Authentication**

    Authentication is applicable only when the publisher you want to get
    fulltext from requires it. OA publishers shouldn't need it as you'd
    expect, and there's some papers from typically closed publishers
    that are open (a good way to check this is the license on the paper [
    see `rcrossref`]). There's many publishers that don't share links at all,
    so they are irrelevant here.

    For publishers that required authentication, the Crossref TDM
    program allows for a single token to authenticate across publishers
    (to make it easier for text miners). The publishers involved with the
    authentication scheme are really only Elsevier and Wiley - these two
    publishers make up a lot of the papers out there and a lot of the
    links on the Crossref API.

    There's a how to guide for Crossref TDM at
    <http://tdmsupport.crossref.org/researchers/>.
    Get your Crossref TDM token by registering at
    <https://apps.crossref.org/clickthrough/researchers>

  **IP addresses**

    If you don't know what IP addresses are, check out
    <https://en.wikipedia.org/wiki/IP_address>. At least Elsevier and
    I think Wiley also check your IP address in addition to requiring the
    authentication token. Usually your're good if you're physically at the
    institution that has access to the publishers content OR on a VPN
    (i.e., pretending you're there).

    If you forget about this, you'll get errors about not being authorized.
    So check and make sure you're on a VPN if you're not physically
    located at your institution.

  **Fences**

    There's yet another issue to worry about. At least with Elsevier, they
    have a so-called "fence" - that is, even if an institution has access
    to Elsevier content, Elsevier doesn't necessarily have the fence
    turned off - if its not off, you can't get through - if it's off, you can.
    If you have the right token and you are sure you're on the right
    IP address, this could be the problem for your lack of access. If that happens
    get in touch with me at <mailto:scott@ropensci.org> and i'll try to sort it out.

  
  |
  |
  |
  '''
  def __init__(self, mailto = None, tdmkey = None):
    self.tdm_key = tdmkey
    self.mailto = mailto

  def __repr__(self):
    return """< %s \ntdm_key: %s\nmailto: %s\n>""" % (type(self).__name__,
        sub_str(self.tdm_key), self.mailto)

  def search(self, ids=None, member=None, filter=None, limit=500, **kwargs):
    '''
    Search Crossref to get text mining links

    :param ids: [Array] DOIs (digital object identifier) or other identifiers
    :param member: [String] member ids
    :param filter: [Hash] Filter options. See ...
    :param limit: [Fixnum] Number of results to return. Not relavant when
        searching with specific dois. Default: 20. Max: 1000
    :param kwargs: any additional arguments will be passed on to
        ``requests.get``

    :return: object of class :class:`~pyminer.Mined`

    Usage::

        # search for many
        from pyminer import Miner
        m = Miner()
        x = m.search(filter = {'has_full_text': True}, limit = 5)
        x
        x.items
        x.links()
        x.links_verbose()
        x.links_unspecified()
        x.result
        x.fetch()

        # get by DOI
        from pyminer import Miner
        m = Miner()
        x = m.search(ids = '10.1371/journal.pone.0033693')
        x
        x.items
        x.items.keys()
        x.links()
        x.links_verbose()
        x.fetch()

        from pyminer import Miner
        m = Miner()
        x = m.search(ids = '10.3897/rio.2.e10445')
        x
        x.links()
        x.links_verbose()
        out = x.fetch()
        out
        out[0].url
        out[0].path
        out[0].type
        out[0].parse()

        ## many at once
        dois = ["10.3897/zookeys.634.9262", "10.3897/zookeys.634.10207", "10.3897/zookeys.634.9917"]
        x = m.search(ids = dois)
        x
        x.links()
        x.links_verbose()
        out = x.fetch()
        out
        out[0].url
        out[0].path
        out[0].type
        out[0].parse()
        
        # filters
        m.search(filter = {
          'full_text_type': 'text/plain', 
          'license_url': "http://creativecommons.org/licenses/by-nc-nd/3.0"})
        m.search(filter = {
          'has_full_text': True, 
          'license_url': "http://creativecommons.org/licenses/by/4.0"})
    '''
    cr = Crossref(mailto = self.mailto)
    if ids is not None:
        limit = None
    res = cr.works(ids = ids, limit = limit, filter = filter, **kwargs)
    return Mined(res, self.tdm_key)
