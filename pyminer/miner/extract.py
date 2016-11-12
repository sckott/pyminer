from ..crutils import *
import textract

def extract(path):
    '''
    Extract full text fro pdf's

    :param path: [String] Path to a pdf file downloaded via {fetch}, or another way.

    :return: [str] a string of text

    Usage::

        import pyminer

        # a pdf
        url = "http://www.banglajol.info/index.php/AJMBR/article/viewFile/25509/17126"
        out = pyminer.fetch(url)
        out.parse()

        # search first, then pass links to fetch
        res = pyminer.search(filter = {'has_full_text': True, 'license_url': "http://creativecommons.org/licenses/by/4.0"})
        # url = res.links_pdf()[0]
        url = 'http://www.nepjol.info/index.php/JSAN/article/viewFile/13527/10928'
        x = pyminer.fetch(url)
        pyminer.extract(x.path)
    '''
    text = textract.process(path)
    return text
