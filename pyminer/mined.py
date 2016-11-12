from .parsers import parse_xml, parse_plain, parse_pdf

class Mined(object):
  """docstring for Mined"""
  def __init__(self, url, path, type):
    super(Mined, self).__init__()
    self.url = url
    self.path = path
    self.type = type

  def parse(self):
    if self.type == "xml" or self.type == "html":
      return parse_xml(self.path)
    elif self.type == "plain":
      return parse_plain(self.path)
    elif self.type == "pdf":
      return parse_pdf(self.path)
    else:
      raise Exception("no parsing method for " + self.type)
