'''
Function:
    Search codes from StackOverflow
Author:
    Zhenchao Jin
WeChat public account:
    Charles_pikachu
'''
import os
import re
import html
import pyflakes
import subprocess
from .baseengine import BaseEngine


'''StackOverflow'''
class StackOverflow(BaseEngine):
    def __init__(self, keyword, proxies={}, **kwargs):
        super(StackOverflow, self).__init__(keyword=keyword, proxies=proxies, **kwargs)
    '''auto coding'''
    def autocoding(self, **kwargs):
        answers = self.search()
        for answer in answers['items']:
            link = answer['link']
            code = self.parse(link)
            if code: break
        if kwargs.get('return_code', True): return code
        ctx = compile(code, '', 'exec')
        return exec(ctx, kwargs.get('globals', {}), kwargs.get('locals', {}))
    '''try to check the correctness of the codes'''
    def checker(self, code):
        # try to check whether the codes can be compiled
        try:
            ctx = compile(code, '', 'exec')
            exec(ctx)
        except:
            return False
        # try to check the grammar of the codes
        tmpfilepath = os.path.join(self.rootdir, 'tmp.py')
        fp = open(tmpfilepath, 'w')
        fp.write(code)
        fp.close()
        p = subprocess.run(f'pyflakes {tmpfilepath}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.remove(tmpfilepath)
        if len(p.stdout) > 0: return False
        return True
    '''search the suitable codes from StackOverflow'''
    def search(self):
        keyword = self.keyword.lower().replace('stackoverflow.', '').replace('_', ' ')
        params = {
            'order': 'desc',
            'sort': 'votes',
            'tagged': 'python',
            'site': 'stackoverflow',
            "intitle": keyword,
        }
        answers = self.session.get(f'{self.api_url}/search', params=params).json()
        if not answers['items']: raise RuntimeError('Fail to search the suitable codes from StackOverflow')
        return answers
    '''parse the codes from html'''
    def parse(self, url):
        response = self.session.get(url, headers=self.headers)
        answers = re.findall(r'<div id="answer-.*?</table', response.text, re.DOTALL)
        def votecount(x):
            r = int(re.search(r'\D(\d{1,5})\D', x).group(1))
            return -r
        for answer in sorted(answers, key=votecount):
            codez = re.finditer(r'<pre[^>]*>[^<]*<code[^>]*>((?:\s|[^<]|<span[^>]*>[^<]+</span>)*)</code></pre>', answer)
            codez = map(lambda x: x.group(1), codez)
            for code in sorted(codez, key=lambda x: -len(x)):
                code = html.unescape(code)
                code = re.sub(r'<[^>]+>([^<]*)<[^>]*>', '\1', code)
                if self.checker(code): return code
        return False