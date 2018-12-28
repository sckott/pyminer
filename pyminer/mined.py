from .crutils import *
from .fetcher import Fetcher

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
    items = self.prep_links()
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
    items = self.prep_links()
    return [ z['link'][0] for z in items ]

  def fetch(self, type = "xml"):
    '''
    Fetch articles

    :param type: [String] one of pdf, xml, plain, html, unspecified
    :return: list of objects of class Fetched

    Usage::

        from pyminer import Miner
        import os
        m = Miner(mailto = os.environ['crossref_email'])
        x = m.search(ids = '10.3897/rio.2.e10445')
        x
        out = x.fetch(type = "pdf")
        out
        out[0].url
        out[0].path
        out[0].type
        out[0].parse()

        from pyminer import Miner
        import os
        m = Miner(mailto = os.environ['crossref_email'], tdmkey = os.environ['CROSSREF_TDM'])
        x = m.search(ids = "10.1016/j.funeco.2010.11.003")
        out = x.fetch(type = "xml")
        out
        out[0].path
        out[0].parse()

        x = m.search(ids = "10.1111/apt.13556")
        out = x.fetch(type = "unspecified")
        out
        out[0].path
        out[0].parse()
    '''
    # get crossref member id
    z = self.prep_links()
    dat = [ {'member': w['member'], 'links': w['link']} for w in z ]
    put = []
    for i in dat:
      types = [ v['content-type'] for v in i['links'] ]
      if type not in content_type2type(types):
         raise ValueError('type ' + type + ' not found in links')
      headers = cr_auth(i, type, self.tdm_key)
      link = pluck_type(i['links'], type)[0]
      put.append({'member': i['member'], 'link': link, 'headers': headers})
    
    tt = []
    for x in put:
      res = Fetcher(x['link'], x['headers']).perform()
      tt.append(res)
    return tt



  # internal methods
  def prep_links(self):
    if self.type == "work":
      items = []
      items.append(self.items)
    else:
      items = self.items
    return items

  def __match_type(self, type):
    items = self.prep_links()
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

def content_type2type(h):
  options = {
    'application/pdf' : 'pdf',
    'application/xml' : 'xml',
    'text/xml' : 'xml',
    'unspecified' : 'unspecified'
  }
  return [ options.get(v) for v in h ]

def type2content_type(h):
  options = {
    'pdf': 'application/pdf',
    'xml': 'application/xml',
    'xml': 'text/xml',
    'unspecified': 'unspecified'
  }
  return options.get(h)

def pluck_type(x, type):
  return compact(
    [ a['URL'] if a['content-type'] == type2content_type(type) else None for a in x ]
  )

def cr_auth(d, type, key):
  mem = d['member']
  if mem is None: 
    return {}
  if mem not in ['78', '263', '311']:
    return {}
  type = type2content_type(type)
  if mem in ['78', '311']:
    return {'CR-Clickthrough-Client-Token': key, 'Accept': type}
  elif mem == '263':
    return {'CR-TDM-Client_Token': key, 'Accept': type}
  else:
    raise ValueError('only these Crossref members supported for passing the\n Crossref TDM token in the request header: 78, 311, 263')
