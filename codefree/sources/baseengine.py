'''
Function:
    Base class for searching codes
Author:
    Zhenchao Jin
WeChat public account:
    Charles_pikachu
'''
import os
import requests


'''Base class for searching codes'''
class BaseEngine():
    def __init__(self, keyword, proxies={}, **kwargs):
        self.rootdir = os.path.split(os.path.abspath(__file__))[0]
        self.keyword = keyword
        self.session = requests.Session()
        self.session.proxies.update(proxies)
        self.api_url = 'https://api.stackexchange.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
        }
        for key, value in kwargs.items(): setattr(self, key, value)
    '''call'''
    def __call__(self, **kwargs):
        return self.autocoding(**kwargs)
    '''auto coding'''
    def autocoding(self, **kwargs):
        raise NotImplementedError('not to be implemented')