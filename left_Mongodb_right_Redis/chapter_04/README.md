## 概述

为了巩固 MongoDB 的增加、 删除、 修改、 查找功能， 本章
将带领读者制作一个简易的员工管理系统。

## 运行环境

- 1.进入项目所在目录(project_1)
- 2.建立项目所需的 python 环境

```java
pipenv install
```

- 3.进入虚拟环境

```java
pipenv shell
```

- 4.启动项目
  **vscode 的 terminal 是 git**

```java
export FLASK_APP=main.py
flask run
```

**vscode 的 terminal 是 cmd**

```java
set FLASK_APP=main.py & flask run
```

**vscode 的 terminal 是 PowerShell**

```java
$env:FLASK_APP=".\main.py" | flask run
```

- 5.访问地址

http://127.0.0.1:5000

![图片](https://github.com/yinian/python/blob/master/left_Mongodb_right_Redis/chapter_04/project_1/imgs/01.png)
