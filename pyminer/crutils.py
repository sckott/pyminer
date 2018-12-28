import re
import requests
from . import __version__

class NoResultException(Exception):
    pass

def make_ua():
    requa = 'python-requests/' + requests.__version__
    pymua = 'pyminer/%s' % __version__
    ua = requa + ' ' + pymua
    str = {
      'User-Agent': ua,
      'X-USER-AGENT': ua
    }
    return str

def is_json(x):
  if re.search('json', x.headers['Content-Type']).__class__.__name__ == 'NoneType':
    return False
  else:
    return True

def parse_json_err(x):
  return x.json()['message'][0]['message']

def check_json(x):
  ctype = x.headers['Content-Type']
  matched = re.match("application/json", ctype)
  if matched.__class__.__name__ == 'NoneType':
    scode = x.status_code
    if str(x.text) == "Not implemented.":
      scode = 400
    raise RequestError(scode, str(x.text))

def sub_str(x, n = 3):
  if(x.__class__.__name__ == 'NoneType'):
    pass
  else:
    return str(x[:n]) + '***'
    
