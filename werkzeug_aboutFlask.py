def run_simple(hostname, port, application, use_reloader=False,
               use_debugger=False, use_evalex=True,
               extra_files=None, reloader_interval=1,
               reloader_type='auto', threaded=False,
               processes=1, request_handler=None, static_files=None,
               passthrough_errors=False, ssl_context=None):
    



def execute(app):
    application_iter = app(environ, start_response)
    try:
        for data in application_iter:
            write(data)
        if not headers_sent:
            write(b'')
    finally:
        if hasattr(application_iter, 'close'):
            application_iter.close()
        application_iter = None