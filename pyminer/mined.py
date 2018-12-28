from .crutils import *
from .fetch import fetch

class Mined(object):
  '''
  Mined: response class for mining Crossref articles
  
  |
  |

  **Mined Methods**

  * links - :func:`~pyminer.Mined.links`
  * links_pdf - :func:`~pyminer.Mined.links_pdf`
  * links_xml - :func:`~pyminer.Mined.links_xml`
  * links_plain - :func:`~pyminer.Mined.links_plain`
  * links_unspecified - :func:`~pyminer.Mined.links_unspecified`
  * links_verbose - :func:`~pyminer.Mined.links_verbose`
  * fetch - :func:`~pyminer.Mined.fetch`
  * extract - :func:`~pyminer.Mined.extract`
  
  |
  |
  |
  '''
  def __init__(self, result, tdm_key = None):
    self.tdm_key = tdm_key
    self.result = result
    self.no_results = ''
    self.type = self.result["message-type"]
    
    if self.result["message-type"] == "work-list":
      self.items = self.result['message']['items']
      self.no_results = len(self.items)
    else:
      self.items = self.result['message']
      self.no_results = 1

  def __repr__(self):
    return '<pyminer search:> \n  results: ' + str(self.no_results)

  def links(self):
    '''
    Get all links

    :return: list with links; empty list if no results

    Usage::

        from pyminer import Miner
        m = Miner()
        x = m.search(ids = '10.1371/journal.pone.0033693')
        x.links()
    '''
    items = self.__prep_links()
    ff = list(filter(None, [ z.get('link') for z in items ]))
    return [ x[0].get('URL') for x in ff ]

  def links_pdf(self):
    '''
    Get links with content-type of "application/pdf"

    :return: list with pdf links; empty list if no results

    Usage::

        from pyminer import Miner
        m = Miner()
        x = m.search(ids = '10.3897/rio.2.e10445')
        x.links_pdf()
    '''
    return self.__match_type("application/pdf")

  def links_xml(self):
    '''
    Get links with content-type of "text/xml"

    :return: list with xml links; empty list if no results

    Usage::

        from pyminer import Miner
        m = Miner()
        x = m.search(ids = '10.3897/rio.2.e10445')
        x.links_xml()
    '''
    return self.__match_type("text/xml")

  def links_plain(self):
    '''
    Get links with content-type of "text/plain"

    :return: list with plain text links; empty list if no results

    Usage::

        from pyminer import Miner
        m = Miner()
        x = m.search(ids = '10.3897/rio.2.e10445')
        x.links_plain()
    '''
    return self.__match_type("text/plain")

  def links_unspecified(self):
    '''
    Get links that have content-type as "unspecified"

    :return: list with links; empty list if no results

    Usage::

        from pyminer import Miner
        m = Miner()
        x = m.search(ids = '10.3897/rio.2.e10445')
        x.links_plain()
    '''
    return self.__match_type("unspecified")

  def links_verbose(self):
    '''
    Get all link metadata

    :return: list of dicts; empty list if no results

    Usage::

        from pyminer import Miner
        m = Miner()
        x = m.search(ids = '10.3897/rio.2.e10445')
        x.links_verbose()
    '''
    items = self.__prep_links()
    return [ z['link'][0] for z in items ]

  def fetch(self):
    '''
    Fetch articles

    :return: list of objects of class Fetched

    Usage::

        from pyminer import Miner
        m = Miner()
        x = m.search(ids = '10.3897/rio.2.e10445')
        out = x.fetch()
        out
        out[0].url
        out[0].path
        out[0].type
        out[0].parse()
    '''
    lks = self.links()
    out = []
    for x in lks:
      res = fetch(x)
      out.append(res)
    return out



  # internal methods
  def __prep_links(self):
    if self.type == "work":
      items = []
      items.append(self.items)
    else:
      items = self.items
    return items

  def __match_type(self, type):
    items = self.__prep_links()
    out = [
      index_safe(compact(
        [ a['URL'] if a['content-type'] == type else None for a in z['link'] ]
      ), 0) for z in items
    ]
    return compact(out)


# helper methods
def compact(z):
  return [x for x in z if x is not None]

def index_safe(x, index):
  try:
    return x[index]
  except:
    return None
