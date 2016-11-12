from ..miner_utils import *

def parse_xml(x):
    '''
    parse xml

    :param path: [String] Path to an xml file
    :return: object of class lxml.etree._Element

    Usage::

        from pyminer import fetch
        from pyminer import parsers
        url = "https://peerj.com/articles/cs-23.xml"
        out = fetch(url)
        parsers.parse_xml(out.path)
    '''
    text = read_disk(x)
    xmlparser = etree.XMLParser()
    tt = etree.fromstring(text, xmlparser)
    return tt

def parse_xml_string(x, encoding = "UTF-8"):
    '''
    parse xml to a string

    :param path: [String] Path to an xml file
    :return: a string

    Usage::

        from pyminer import fetch
        from pyminer import parsers
        url = "https://peerj.com/articles/cs-23.xml"
        out = fetch(url)
        parsers.parse_xml_string(out.path)
    '''
    tmp = parse_xml(x)
    return etree.tostring(tmp, method = "text", encoding = encoding)

def parse_plain(x):
    '''
    parse plain text

    :param path: [String] Path to a plain text file
    :return: a string

    Usage::

        from pyminer import fetch
        from pyminer import parsers
        url = "xx"
        out = fetch(url)
        parsers.parse_plain(out.path)
    '''
    return read_disk(x)

def parse_pdf(x):
    '''
    parse pdf

    :param path: [String] Path to a pdf file
    :return: a string

    Usage::

        from pyminer import fetch
        from pyminer import parsers
        url = "http://www.banglajol.info/index.php/AJMBR/article/viewFile/25509/17126"
        out = fetch(url)
        parsers.parse_pdf(out.path)
    '''
    return extract(x)
