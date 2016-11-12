import uuid
import re
from .extract import extract
from lxml import etree

# content and file types
def detect_type(x):
  ctype = x.headers['Content-Type']
  if re.match('text/xml|application/xml', ctype) is not None:
    return 'xml'
  elif re.match('text/html|application/html', ctype) is not None:
    return 'html'
  elif re.match('text/plain', ctype) is not None:
    return 'plain'
  elif re.match('application/pdf', ctype) is not None:
    return 'pdf'
  else:
    return "unspecified"

def make_ext(x):
  if x == 'xml':
    return 'xml'
  elif x == 'html':
    return 'html'
  elif x == 'plain':
    return 'txt'
  elif x == 'pdf':
    return 'pdf'
  else:
    return "txt"

def make_path(type):
  type = make_ext(type)
  uu = str(uuid.uuid4())
  path = uu + '.' + type
  return path



# read and write
def write_disk(res, path):
  f = open(path, 'wb')
  f.write(res.content)
  f.close()

def read_disk(path):
  f = open(path, 'r')
  dat = f.read()
  f.close()
  return dat


# publisher checks
def is_elsevier_wiley(x):
  pass
  # tmp = x.match 'elsevier|wiley'
  # !tmp.nil?
