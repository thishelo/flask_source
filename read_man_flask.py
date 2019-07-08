# coding=UTF-8
"""启动流程：
	1、执行实例对象.run()方法
	2、执行werkzeug的run_simple()
	3、execut(app)
	4、__call_()返回self.wsgi_app(environ, start_response)
	5、wsgi_app()处理request和session
	6、执行视图函数response = self.full_dispatch_request()
	7、对返回值进行封装    return self.finalize_request(rv)
	8、return response(environ, start_response)处理好的内容返回给浏览器
"""

from __future__ import with_statement
import os
import sys

from jinja2 import Environment, PackageLoader, FileSystemLoader
from werkzeug import Request as RequestBase, Response as ResponseBase, \
	LocalStack, LocalProxy, create_environ, shareDataMiddleware





class Request(ResponseBase):
	"""docstring for Request"""
	def __init__(self, arg):
		super(Request, self).__init__()
		self.arg = arg

class Response(ResponseBase):
	"""docstring for Response"""
	def __init__(self, arg):
		super(Response, self).__init__()
		self.arg = arg
		
class _RequestGlobals(object):
	"""docstring for _RequestGlobals"""
	def __init__(self, arg):
		super(_RequestGlobals, self).__init__()
		self.arg = arg

class _RequetContext(object):
	"""docstring for _RequetContext"""
	def __init__(self, arg):
		super(_RequetContext, self).__init__()
		self.arg = arg



		
		
class Falsk(object):
	"""docstring for Falsk"""
	def __init__(self, arg):
		super(Falsk, self).__init__()
		self.arg = arg
		

		
		