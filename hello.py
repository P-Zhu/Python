# hello.py
# --version python3


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    path = environ['PATH_INFO'].encode('iso-8859-1').decode('utf8')[1:]
    body = '<h1>Hello, %s!</h1>' % (path or 'web')
    return [body.encode('utf-8')]


# 苷
