import random
import os, os.path
import cherrypy

f_string = ['Подходит поручик Ржевский к Наташе Ростовой', "Купил мужик шляпу", "подходит мужчина к гинекологу"]
s_string = [' а она ему как раз', ' сел в машину и сгорел', ' а там армяне в нарды играют', ' а она до самого хуя']

def html_gen(string):
    return """<html>
          <head>
          <link href="/static/css/style.css" rel="stylesheet">
          </head>
          <body>
          <h2 style="text-align: center;"><font color = "white">{}</font></h2>
          </body>
        </html>""".format(string)



class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        string = random.choice(f_string) + random.choice(s_string)
        return html_gen(string)

if __name__ == '__main__':
    conf = {
            '/': {
                'tools.sessions.on': True,
                'tools.staticdir.root': os.path.abspath(os.getcwd())
                },
                '/static': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': './public'
                }
            }
    cherrypy.quickstart(StringGenerator(), '/', conf)
