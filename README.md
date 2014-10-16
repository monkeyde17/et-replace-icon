替换android项目下的icon
=======================

这两天app要换icon，想想又要去一个一个复制进去，想想就觉得不是程序员该干的事情。

碰巧昨天稍微看了[PNG](http://blog.csdn.net/bisword/article/details/2777121)的文件格式
所以，现在用`python`做一个批处理的脚本。

## 需求

* 识别`PNG`的`iHDR`信息来识别分辨率
* 复制到对应文件夹下，这里写成配置文件形式
    例如：72|72|/proj.android/res/drawable-hdpi|

## 用法

* 配置好`config.in`，用`|`作为分隔符号，例如`72|72|/proj.android/res/drawable-hdpi|`
* 运行`./run.sh`


PS : +.= python代码写得好搓！

----------------------------------------------

- [ ] 这周找个时间重新写下这个python的代码=。=

- [ ] 添加图片压缩的功能 

可以再看看[PNG](http://blog.csdn.net/bisword/article/details/2777121)的文件格式
看看怎么把一个`72*72`的压缩到`48*48`的。

by etond 20141016


