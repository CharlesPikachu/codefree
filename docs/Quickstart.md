# 快速开始

#### 代码搜索

示例代码如下:

```python
from codefree import codefree

engine = codefree.CodeFree(keyword='quick sort')
code = engine(return_code=True)
print(code)
```

CodeFree实例化时的参数解释如下:

- keyword: 搜索的关键词;
- source: 使用的代码源, 目前只支持"stackoverflow";
- proxies: 使用的代理, 代理格式同[Requests](https://docs.python-requests.org/)。

run函数支持的参数如下:

- return_code: 是否返回代码, 代码搜索时必须设为True。

#### 代码运行

示例代码如下:

```python
from codefree import codefree

engine = codefree.CodeFree(keyword='quick sort')
lst = [2, 5, 1, 4, 6, 10, 3]
g = {'lst': lst}
engine(return_code=False, globals=g, following_code='result = quickSort(lst)')
print(g['result'])
```

- following_code: 添加的补充代码, 用于保证搜索到的代码可以正常运行;
- globals: 字典类型, 用于定义代码中的未知变量;
- return_code: 是否返回代码, 代码运行时必须设为False。

效果如下:

<div align="center">
  <img src="https://github.com/CharlesPikachu/codefree/raw/master/docs/screenshot.gif" width="600"/>
</div>
<br />