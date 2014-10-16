替换android项目下的icon
=======================

这两天app要换icon，想想又要去一个一个复制进去，想想就觉得不是程序员该干的事情。

碰巧昨天稍微看了[PNG](http://blog.csdn.net/bisword/article/details/2777121)的文件格式
所以，现在用`python`做一个批处理的脚本。

## 需求

* 识别`PNG`的`iHDR`信息来识别分辨率
* 复制到对应文件夹下，这里写成配置文件形式
    例如：[72] = ./proj.android/res/drawable-hdpi

## 用法

有待更新 =。= 
