from .crutils import *
from .miner import Miner

def fetch(url):
    '''
    Get full text

    Work easily for open access papers, but for closed. For non-OA papers, use
    Crossref's Text and Data Mining service, which requires authentication and
    pre-authorized IP address. Go to https://apps.crossref.org/clickthrough/researchers
    to sign up for the TDM service, to get your key. The only publishers
    taking part at this time are Elsevier and Wiley.

    :param url: [String] A url for full text

    :return: [Mined] An object of class Mined, with methods for extracting
    the url requested, the file path, and parsing the plain text, XML, or extracting
    text from the pdf.

    XML returns object of class lxml.etree._Element, which you can parse using
    for example lxml

    Usage::

        import pyminer

        # pdf
        url = "http://www.banglajol.info/index.php/AJMBR/article/viewFile/25509/17126"
        out = pyminer.fetch(url)
        out.url
        out.path
        out.type
        out.parse()

        # xml
        url = "https://peerj.com/articles/cs-23.xml"
        out = pyminer.fetch(url)
        out.url
        out.path
        out.type
        out.parse()
        ## or drop down to individual parsing methods
        from pyminer import parsers as p
        p.parse_xml(out.path)
        p.parse_xml_string(out.path)

        # search first, then pass links to fetch
        res = pyminer.search()
        pyminer.fetch(res['url'])
    '''
    return Miner(url).perform()
