# 学习Flask源码笔记

##启动流程：
###	1、执行实例对象.run()方法
###	2、执行werkzeug的run_simple()
###	3、execut(app)
###	4、__call_()返回self.wsgi_app(environ, start_response)
###	5、wsgi_app()处理request和session
###	6、执行视图函数response = self.full_dispatch_request()
###	7、对返回值进行封装    return self.finalize_request(rv)
###	8、return response(environ, start_response)处理好的内容返回给浏览器
