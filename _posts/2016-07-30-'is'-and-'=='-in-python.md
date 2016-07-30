---
published: true
title: Python中'is'和'=='的区别
layout: post
author: linnet8989
category: Blogs
tags:
- python
- python3
- tutorial
---

## 一切皆对象
在Python中，一切皆对象，而对象包含三要素：id、type、value，其中id是唯一标识，value是对象的值。

## 'is'和'=='的区别
'is'对比的是对象的id。一般情况下，在Python中每次赋值或引用未定义的值就会新建一个对象，所以像 `a is 200` 这样的判断是万万不可的，但是Python会将256以下的数字优化为常量定义，也就是说不会新建对象，实际的结果却会出现 `True` 。而字符串也会有相似的现象出现，感兴趣的可以自己试试。'is'的常见用法如下：

```python
a = [1, 2, 3]
# 值为可变（immutable）对象的变量的赋值是引用赋值，
# 即不会新建对象，如list、dict、set
b = a
print(a is b) # True

class MyClass:
    pass
c = MyClass()
d = c
print(c is d) # True

# 以下为内建常量
print(False is False) # True
print(None is None) # True
```

'=='对比的是对象的value。很好理解，这里就不多费笔墨了。  

## 后记
说到比较就很容易联系到 `if` 这样条件语句，以后还会写篇博文介绍一下。