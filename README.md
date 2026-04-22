# pyminer

> [!WARNING]
> Crossref retired their text and data mining support in 2020, see <https://www.crossref.org/blog/evolving-our-support-for-text-and-data-mining/>

Python client for text mining leveraging [Crossrefs Text and Data Mining service](http://tdmsupport.crossref.org/researchers).

## Installation

```console
git clone https://github.com/sckott/pyminer.git
cd pyminer
uv pip install .
```

## Search

Strongly recommend for search using your email in the mailto parameter in the Miner() call to get in the "fast lane".

```python
from pyminer import Miner
import os
m = Miner(mailto = os.environ['crossref_email'])
m.search(filter = {'has_full_text': True}, limit = 5)
```

## Fetch

If you have a Crossref Text and Data Mining key/token, you can give it in the tdm_key parameter in the Miner() call

```python
# a Pensoft article
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

# an Elsevier article - BEWARE, they check IP addresses, so your IP address
# must be at a member institution or similar
from pyminer import Miner
import os
m = Miner(mailto = os.environ['crossref_email'], tdm_key = os.environ['CROSSREF_TDM'])
x = m.search(ids = "10.1016/j.funeco.2010.11.003")
out = x.fetch(type = "xml")
out
out[0].path
out[0].parse()
```

## Extract

```python
from pyminer import fetch, extract
url = 'http://www.nepjol.info/index.php/JSAN/article/viewFile/13527/10928'
x = fetch(url)
extract(x.path)
```

## Meta

- License: MIT, see [LICENSE file](LICENSE.md)
- Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.
