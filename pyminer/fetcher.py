import requests
from .fetcher_utils import *
from .crutils import *
from .fetched import Fetched

class Fetcher(object):
  """docstring for Fetcher"""
  def __init__(self, url):
    super(Fetcher, self).__init__()
    self.url = url

  def perform(self):
    try:
      r = requests.get(self.url, headers = make_ua())
      r.raise_for_status()
    except requests.exceptions.HTTPError:
      r.raise_for_status()
    except requests.exceptions.RequestException as e:
      print(e)

    type = detect_type(r)
    path = make_path(r, type)
    write_disk(r, path)

    return Fetched(self.url, path, type)
