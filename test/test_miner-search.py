"""Tests for miner module - search methods"""
import os
import pytest
import vcr
from pyminer import miner

@vcr.use_cassette('test/vcr_cassettes/search.yaml')
def test_search():
    "miner.search - basic test"
    res = miner.search(filter = {'has_full_text': True}, limit = 5)
    assert 'Response' == res.__class__.__name__
    assert list == res.items.__class__
    assert dict == res.result.__class__
    assert 'method' == res.links.__class__.__name__

@vcr.use_cassette('test/vcr_cassettes/search_limit.yaml')
def test_search_limit():
    "miner.search - limit"
    res = miner.search(filter = {'has_full_text': True}, limit = 1)
    assert 'Response' == res.__class__.__name__
    assert 1 == len(res.items)

# def test_search_filter():
#     "miner.search - diff taxonKey2"
#     res = miner.search()
#     assert 'dict' == res.__class__.__name__
#     assert 6 == len(res)
#     assert 2683264 == res['results'][0]['taxonKey']
