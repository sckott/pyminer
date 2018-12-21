import requests
from .miner_utils import *
from .crutils import *
from .mined import Mined

class Miner(object):
  """docstring for Miner"""
  def __init__(self, url):
    super(Miner, self).__init__()
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

    return Mined(self.url, path, type)
