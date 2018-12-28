import requests
from .fetcher_utils import *
from .crutils import *
from .fetched import Fetched

class Fetcher(object):
  """docstring for Fetcher"""
  def __init__(self, url, headers = {}):
    super(Fetcher, self).__init__()
    self.url = url
    self.headers = headers

  def perform(self):
    try:
      ua = make_ua()
      ua.update(self.headers)
      r = requests.get(self.url, headers = ua)
      r.raise_for_status()
    except requests.exceptions.HTTPError:
      r.raise_for_status()
    except requests.exceptions.RequestException as e:
      print(e)

    type = detect_type(r)
    path = make_path(r, type)
    write_disk(r, path)

    return Fetched(self.url, path, type)
