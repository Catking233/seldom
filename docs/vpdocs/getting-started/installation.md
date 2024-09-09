# Installation

seldom的安装非常简单。

* 快速安装

目前已经上传 pypi.org ,可以使用pip命令安装。

```shell
> pip install seldom
```

* 体验最新代码

如果你想随时体验最新的代码，可以使用下面的命令。

```shell
> pip install -U git+https://github.com/defnngj/seldom.git@master
```

* 安装依赖

随着seldom 加入更多的功能，seldom不得不依赖其他的开源库。你可以在 requirements.txt 文件里面看到这些依赖。

```shell
Appium-Python-Client>=4.1.0
XTestRunner>=1.7.2
loguru>=0.7.0
openpyxl>=3.0.3
pyyaml>=6.0
jsonschema>=4.10.0
jmespath>=0.10.0
pymysql>=1.0.0
genson==1.2.2
click~=8.1.3
python-dateutil==2.8.2
```

先通过 `pip` 命令安装这些依赖库，可以加快seldom的安装。

```shell
> pip install -r requirements.txt
```

* 检查安装

最后，我们可以通过`pip show seldom`命令检查安装。

```shell
> pip show seldom

Name: seldom
Version: 3.x.x
Summary: Seldom automation testing framework based on unittest.
Home-page: https://seldomqa.github.io
Author: bugmaster
Author-email: fnngj@126.com
License: Apache-2.0
Location: C:\Python311\Lib\site-packages
Requires:  Appium-Python-Client, click, genson, jmespath, jsonschema, loguru, openpyxl, pymysql, python-dateutil, pyyaml, requests, websocket-client, XTestRunner
Required-by:
```
