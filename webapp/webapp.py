# -*- coding:utf-8 -*-

from bottle import route, run, default_app

@route('/')
def hello():
    return "Hello World!"

if __name__ == "__main__":
    run(host='localhost', port=80, debug=True)
else:
    #WSGI default call is "application"
    application = default_app()
