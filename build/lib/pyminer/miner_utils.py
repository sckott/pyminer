import uuid
import re
import os
from .miner import extract
from lxml import etree
from appdirs import *

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
  base_path = user_cache_dir('pyminer')
  if not os.path.exists(base_path):
    os.makedirs(base_path)
  path = base_path + '/' + uu + '.' + type
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
