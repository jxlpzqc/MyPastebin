# 任务报告  
任务二：My Pastebin  

---
## 项目介绍
就是一个Pastebin！用Python3编写
## 所需要的库  
- Flask  
- Flask-SQLAlchemy  
- pymysql  
```
pip install Flask
pip install Flask-SQLAlchemy
pip install pymysql
```
## 实现细节
1. 采用Flask MVC框架和Flask-SQLALchemy ORM库，实现了基本功能  
2. 采用多线程技术实现了自动过期并清理数据库过期记录  
3. 实现了加密分享  
4. 采用Cookie保存会话，在“阅后即焚”中辨别paste的poster和其他人  
5. 使用可以扩展的方式实现了Syntax的处理器调用  
6. 在处理用户提交字符串时考虑到了\n和空格的处理，并将它们转换成了相应的实体，并且处理了用户所提交的尖括号，也转化成了相应的HTML实体  
7. 前端部分采用了Bootstrap框架，Pastebin的show页通过原生媒体查询方式做了响应式布局  
8. 使用highlight.js实现了代码高亮功能    

## 心得
1. 原先在MVC上，使用过ASP.NET MVC和ThinkPHP，感觉大同小异，感觉Python Flask在代码行数上胜出ASP.NET的C#，ASP.NET在性能上胜出Flask，至于稳定性，我一直没有任何的感觉
2. 同样还是ORM模型，感觉还是大同小异，总体上说，SQLAlchemy的简洁性和代码的行数吸引了我（就像我原来用ADO.NET、JDBC时候EntityFramework给我的感觉差不多）  
3. 感觉Flask进入入门特别快（大概用1-2小时阅读完文档的QuickStart就能开始开发的过程，对于入门者甚至不需要了解MVC的基本结构就能写出这个Pastebin）  
4. 我担心的还是效率问题，担心Python太慢了  

## 缺陷  
1. 由于将用户的字符串的尖括号全部转换成了HTML实体，所以使得在前端实现富文本编辑器成为了不可能，可以通过将全部转换改为过滤<frame><iframe><script><article><style>的方法改进这一问题  
2. 将控制器，启动函数，工具函数和模型都在一个文件写出，大大的增加了耦合性，不便于代码修改和维护，在我的做的[任务5 真课程表](https://github.com/jxlpzqc/TrueNEUSchedule)中通过多文件的方法解决了这个缺陷
3. 在实现这个任务的时候没有使用IDE，但在任务5中学会了使用IDE（PyCharm）  

## 仍未解决的问题  
- 作为一直使用Windows的Developer，服务器系统当然也是Windows，既然服务器系统是Windows，当然倾向选择IIS，问题就处在这里，IIS+Flask怎么部署是一个很大的问题，网上的教程非常的稀缺，我用有限的教程跟着做了一遍，无一不是HTTP 500，所以最后我是采用了那个python web.app的办法让它在我的服务器上跑起来了，但是上面明确写着下面一句话，十分的头疼
  >  WARNING: Do not use the development server in a production environment.  
    Use a production WSGI server instead.  

## Demo
 直接点就好了吧，哈哈  
 [http://host.chengziqiu.top:8080](http://host.chengziqiu.top:8080)

