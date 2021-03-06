pyminer
=======

|pypi| |docs| |travis| |coverage|

Python client for text mining levaraging `Crossrefs Text and Data Mining service
<http://tdmsupport.crossref.org/researchers>`__.

`Source on GitHub at sckott/pyminer <https://github.com/sckott/pyminer>`__

Other Crossref text mining (and related) clients:

* R: `rcrossref`, `ropensci/rcrossref <https://github.com/ropensci/rcrossref>`__
* R: `crminer`, `ropensci/crminer <https://github.com/ropenscilabs/crminer>`__
* R: `fulltext`, `ropensci/fulltext <https://github.com/ropensci/fulltext>`__
* Ruby: `textminer`, `sckott/textminer <https://github.com/sckott/textminer>`__
* Python: `habanero`, `sckott/habanero <https://github.com/sckott/habanero>`__

Installation
============

Stable from pypi

.. code-block:: console

    pip install pyminer

Development version

.. code-block:: console

    [sudo] pip install git+git://github.com/sckott/pyminer.git#egg=pyminer


Search
======

Strongly recommend for search using your email in the mailto parameter in the 
Miner() call to get in the "fast lane".

.. code-block:: python

    from pyminer import Miner
    import os
    m = Miner(mailto = os.environ['crossref_email'])
    m.search(filter = {'has_full_text': True}, limit = 5)


Fetch
=====

If you have a Crossref Text and Data Mining key/token, you can give it in the 
tdmkey parameter in the Miner() call

.. code-block:: python

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
    m = Miner(mailto = os.environ['crossref_email'], tdmkey = os.environ['CROSSREF_TDM'])
    x = m.search(ids = "10.1016/j.funeco.2010.11.003")
    out = x.fetch(type = "xml")
    out
    out[0].path
    out[0].parse()


Extract
=======

.. code-block:: python

    from pyminer import fetch, extract
    url = 'http://www.nepjol.info/index.php/JSAN/article/viewFile/13527/10928'
    x = fetch(url)
    extract(x.path)

Meta
====

* License: MIT, see `LICENSE file <LICENSE>`__
* Please note that this project is released with a `Contributor Code of Conduct <CODE_OF_CONDUCT.md>`__. By participating in this project you agree to abide by its terms.

.. |pypi| image:: https://img.shields.io/pypi/v/pyminer.svg
   :target: https://pypi.python.org/pypi/pyminer

.. |docs| image:: https://readthedocs.org/projects/pyminer/badge/?version=latest
   :target: http://pyminer.readthedocs.io/en/latest/?badge=latest

.. |travis| image:: https://travis-ci.org/sckott/pyminer.svg
   :target: https://travis-ci.org/sckott/pyminer

.. |coverage| image:: https://coveralls.io/repos/sckott/pyminer/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/sckott/pyminer?branch=master

