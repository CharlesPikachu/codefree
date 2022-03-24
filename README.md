<div align="center">
  <img src="./docs/logo.png" width="600"/>
</div>
<br />

[![docs](https://img.shields.io/badge/docs-latest-blue)](https://codefree.readthedocs.io/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/codefree)](https://pypi.org/project/codefree/)
[![PyPI](https://img.shields.io/pypi/v/codefree)](https://pypi.org/project/codefree)
[![license](https://img.shields.io/github/license/CharlesPikachu/codefree.svg)](https://github.com/CharlesPikachu/codefree/blob/master/LICENSE)
[![PyPI - Downloads](https://pepy.tech/badge/codefree)](https://pypi.org/project/codefree/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/codefree?style=flat-square)](https://pypi.org/project/codefree/)
[![issue resolution](https://isitmaintained.com/badge/resolution/CharlesPikachu/codefree.svg)](https://github.com/CharlesPikachu/codefree/issues)
[![open issues](https://isitmaintained.com/badge/open/CharlesPikachu/codefree.svg)](https://github.com/CharlesPikachu/codefree/issues)

Documents: https://codefree.readthedocs.io/


# CodeFree
```sh
CodeFree: Make no code a reality.
You can star this repository to keep track of the project if it's helpful for you, thank you for your support.
```


# Support Sources
| Source                 | Official Website of the Source                                   | Core Code                                              | Reference                                                   |
| :----:                 | :----:                                                           | :----:                                                 | :----:                                                      |
| Stackoverflow          | [click](https://stackoverflow.com/)                              | [click](./codefree/sources/stackoverflow.py)           | [click](https://github.com/drathier/stack-overflow-import)  |


# Install

#### Pip install
```sh
run "pip install codefree"
```

#### Source code install
```sh
(1) Offline
Step1: git clone https://github.com/CharlesPikachu/codefree.git
Step2: cd codefree -> run "python setup.py install"
(2) Online
run "pip install git+https://github.com/CharlesPikachu/codefree.git@master"
```


# Quick Start

#### Search Code

```python
from codefree import codefree

engine = codefree.CodeFree(keyword='quick sort')
code = engine(return_code=True)
print(code)
```

#### Execute Code

```python
from codefree import codefree

engine = codefree.CodeFree(keyword='quick sort')
lst = [2, 5, 1, 4, 6, 10, 3]
g = {'lst': lst}
engine(return_code=False, globals=g, following_code='result = quickSort(lst)')
print(g['result'])
```


# Screenshot

![img](./docs/screenshot.gif)


# Projects in Charles_pikachu
- [Games](https://github.com/CharlesPikachu/Games): Create interesting games by pure python.
- [DecryptLogin](https://github.com/CharlesPikachu/DecryptLogin): APIs for loginning some websites by using requests.
- [Musicdl](https://github.com/CharlesPikachu/musicdl): A lightweight music downloader written by pure python.
- [Videodl](https://github.com/CharlesPikachu/videodl): A lightweight video downloader written by pure python.
- [Pytools](https://github.com/CharlesPikachu/pytools): Some useful tools written by pure python.
- [PikachuWeChat](https://github.com/CharlesPikachu/pikachuwechat): Play WeChat with itchat-uos.
- [Pydrawing](https://github.com/CharlesPikachu/pydrawing): Beautify your image or video.
- [ImageCompressor](https://github.com/CharlesPikachu/imagecompressor): Image compressors written by pure python.
- [FreeProxy](https://github.com/CharlesPikachu/freeproxy): Collecting free proxies from internet.
- [Paperdl](https://github.com/CharlesPikachu/paperdl): Search and download paper from specific websites.
- [Sciogovterminal](https://github.com/CharlesPikachu/sciogovterminal): Browse "The State Council Information Office of the People's Republic of China" in the terminal.
- [CodeFree](https://github.com/CharlesPikachu/codefree): Make no code a reality.
- [DeepLearningToys](https://github.com/CharlesPikachu/deeplearningtoys): Some deep learning toys implemented in pytorch.
- [DataAnalysis](https://github.com/CharlesPikachu/dataanalysis): Some data analysis projects in charles_pikachu.
- [Imagedl](https://github.com/CharlesPikachu/imagedl): Search and download images from specific websites.


# More
#### WeChat Official Accounts
*Charles_pikachu*  
![img](./docs/pikachu.jpg)