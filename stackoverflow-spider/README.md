#  爬取 Stackoverflow 1m 条问答
基于`spider`实现的爬取工具
## 运行
cd stackoverflow-spider
scrapy crawl stackoverflow

## 保存数据
scrapy crawl stackoverflow -o result.json -t json  

**有关保存路径可以修改**

执行sql.py，保存到mysql数据库

作为一个热爱编程的大学生，怎么能不知道面向 stackoverflow 编程呢。

打开 stackoverflow 主页，在 questions 页面下选择按 vote 排序，爬取前 20000 页，每页将问题数量设置为 50，共 1m 条，（实际上本来是想爬完 13m 条的，但 1m 条后面问题基本上都只有 1 个或 0 个回答，那就选取前 1m 就好吧）  

## 数据可视化暂时未实现

[参考代码](https://github.com/chenjiandongx/stackoverflow-spider)