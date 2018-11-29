#!/usr/bin/python3

import random
import os, os.path
import cherrypy

SITE = 'anek.kz159.ru' #Name of site for cherrypy

PORT = 8080 #default port

f_string = ['Подходит поручик Ржевский к Наташе Ростовой', "Купил мужик шляпу", "подходит мужчина к гинекологу"]
s_string = [' а она ему как раз', ' сел в машину и сгорел', ' а там армяне в нарды играют', ' а она до самого хуя']
authors = ['Navalny', 'Gitlar', 'Albert Einstein', 'Nikola Tesla', 'Alan Turing', 'Benedict Cucumberpech']

def html_gen(string, author):
    return """<html>
          <head>
	  <link href="/static/css/style.css" rel="stylesheet">
	  </head>
          <body>
          <h2 style="text-align: center;"><font color = "white">{}</font></h2>
          <p style="text-align:right;"><cite>&ndash;<font color = "white"; font size="+3>"{}</font></cite></p>
          </body>
        </html>""".format(string, author)

class Root(object):
    @cherrypy.expose
    def index(self):
        string = random.choice(f_string) + random.choice(s_string)
        author = random.choice(authors)
        return html_gen(string, author)

if __name__ == '__main__':
    conf ={
	    'global':{
		'server.socket_port': PORT,
		},
            '/': {
                'tools.sessions.on': True,
	            'tools.proxy.on': True,
        	    'tools.proxy.base': 'http://' + SITE,
                'tools.staticdir.root': os.path.abspath(os.getcwd())
                },
            '/static': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': './public',
                }
}

cherrypy.quickstart(Root(), '/', conf)
