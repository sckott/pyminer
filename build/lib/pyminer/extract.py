from .crutils import *
import pdftotext

def extract(path):
    '''
    Extract full text from pdf's

    :param path: [String] Path to a pdf file downloaded via {fetch}, or another way.

    :return: [str] a string of text

    Usage::

        from pyminer import miner

        # a pdf
        url = "http://www.banglajol.info/index.php/AJMBR/article/viewFile/25509/17126"
        out = miner.fetch(url)
        out.parse()

        # search first, then pass links to fetch
        res = miner.search(filter = {'has_full_text': True, 'license_url': "http://creativecommons.org/licenses/by/4.0"})
        # url = res.links_pdf()[0]
        url = 'http://www.nepjol.info/index.php/JSAN/article/viewFile/13527/10928'
        x = miner.fetch(url)
        miner.extract(x.path)
    '''
    try:
        with open(path, "rb") as f:
            pdf = pdftotext.PDF(f)
        txt = "\n\n".join(pdf)
    except Exception as e:
        raise e
    return txt
