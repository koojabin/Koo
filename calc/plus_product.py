from cgi import parse_qs
from plus_product_template import html

def application(environ, start_response):
    c = parse_qs(environ['QUERY_STRING'])
    a = c.get('a', [''])[0]
    b = c.get('b', [''])[0]
    x = 0
    y = 0
    if a.isdigit() and b.isdigit():
        a, b = int(a), int(b)
        x = a + b
        y = a * b
    response_body = html % {
        'x' : x or 0,
        'y' : y or 0,
        }
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
