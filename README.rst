pyminer
=======

|pypi| |docs| |travis| |coverage|

Python client for the `GBIF API
<http://www.gbif.org/developer/summary>`__.

`Source on GitHub at sckott/pyminer <https://github.com/sckott/pyminer>`__

Other Crossref text mining (and related) clients:

* R: `rcrossref`, `ropensci/rcrossref <https://github.com/ropensci/rcrossref>`__
* R: `crminer`, `ropensci/crminer <https://github.com/ropenscilabs/crminer>`__
* R: `fulltext`, `ropensci/fulltext <https://github.com/ropensci/fulltext>`__
* Ruby: `textminer`, `sckott/textminer <https://github.com/sckott/textminer>`__

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

.. code-block:: python

    from pyminer import Miner
    m.search(filter = {'has_full_text': True}, limit = 5)


Fetch
=====

.. code-block:: python

    from pyminer import fetch
    url = "http://www.banglajol.info/index.php/AJMBR/article/viewFile/25509/17126"
    out = fetch(url)
    out.url
    out.path
    out.type
    out.parse()


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

