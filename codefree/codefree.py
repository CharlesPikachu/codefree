'''
Function:
    Codefree: Make no code a reality.
Author:
    Zhenchao Jin
WeChat public account:
    Charles_pikachu
'''
from .sources import StackOverflow


'''Codefree'''
class CodeFree():
    def __init__(self, keyword, source='stackoverflow', proxies={}, **kwargs):
        self.source = source.lower()
        self.supported_sources = {
            'stackoverflow': StackOverflow
        }
        assert source in self.supported_sources, f'Source {self.source} has not been supported'
        self.selected_source = self.supported_sources[self.source](keyword=keyword, proxies=proxies, **kwargs)
    '''call'''
    def __call__(self, **kwargs):
        return self.selected_source(**kwargs)