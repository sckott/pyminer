"""Tests for miner module - fetch methods"""
import os
import pytest
import vcr
from pyminer import fetch

@vcr.use_cassette('test/vcr_cassettes/fetch.yaml')
def test_fetch():
    "miner.fetch - basic test"
    url = "http://www.banglajol.info/index.php/AJMBR/article/viewFile/25509/17126"
    res = fetch(url)
    assert 'Fetched' == res.__class__.__name__
    assert 'method' == res.parse.__class__.__name__
    # assertIs(res.path, str)
    # assert 'method' == res.links.__class__.__name__

# @vcr.use_cassette('test/vcr_cassettes/fetch_limit.yaml')
# def test_fetch_limit():
#     "miner.fetch - limit"
#     res = miner.fetch(filter = {'has_full_text': True}, limit = 1)
#     assert 'Response' == res.__class__.__name__
#     assert 1 == len(res.items)
