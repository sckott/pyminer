class Response(object):
  '''
  pyminer: response class
  '''
  def __init__(self, result):
    self.result = result
    if self.result["message-type"] == "work-list":
      self.items = self.result['message']['items']
    else:
      self.items = self.result['message']

  def __repr__(self):
    return '<pyminer search:> \n  results: ' + str(len(self.items))

  def links(self):
    return [ compact([ a['URL'] for a in z['link'] ])[0] for z in self.items ]

  def links_pdf(self):
    return match_type(self.items, "application/pdf")

  def links_xml(self):
    return match_type(self.items, "text/xml")

  def links_plain(self):
    return match_type(self.items, "text/plain")

  def links_unspecified(self):
    return match_type(self.items, "unspecified")

  def links_verbose(self):
    return [ z['link'][0] for z in self.result['message']['items'] ]


def match_type(x, type):
  out = [
    index_safe(compact(
      [ a['URL'] if a['content-type'] == type else None for a in z['link'] ]
    ), 0) for z in x
  ]
  return compact(out)

def compact(z):
  return [x for x in z if x is not None]

def index_safe(x, index):
  try:
    return x[index]
  except:
    return None
