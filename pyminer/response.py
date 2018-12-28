from .miner import fetch

class Response(object):
  '''
  pyminer: search response class
  
  |
  |

  **Methods**

  * links - :func:`~pyminer.Response.links`
  * links_pdf - :func:`~pyminer.Response.links_pdf`
  * links_xml - :func:`~pyminer.Response.links_xml`
  * links_plain - :func:`~pyminer.Response.links_plain`
  * links_unspecified - :func:`~pyminer.Response.links_unspecified`
  * links_verbose - :func:`~pyminer.Response.links_verbose`
  * fetch - :func:`~pyminer.Response.fetch`

  '''
  def __init__(self, result):
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
    Get links

    :return: list with links

    Usage::

        from pyminer import miner
        x = miner.search(ids = '10.1371/journal.pone.0033693')
        x.links()
    '''
    items = self.__prep_links()
    ff = list(filter(None, [ z.get('link') for z in items ]))
    return [ x[0].get('URL') for x in ff ]

  def links_pdf(self):
    return self.__match_type("application/pdf")

  def links_xml(self):
    return self.__match_type("text/xml")

  def links_plain(self):
    return self.__match_type("text/plain")

  def links_unspecified(self):
    return self.__match_type("unspecified")

  def links_verbose(self):
    items = self.__prep_links()
    return [ z['link'][0] for z in items ]

  def fetch(self):
    lks = self.links()
    out = []
    for x in lks:
      res = fetch(x)
      out.append(res)
    return out
    # [ fetch(x) for x in lks ]

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

def compact(z):
  return [x for x in z if x is not None]

def index_safe(x, index):
  try:
    return x[index]
  except:
    return None
