import jinja2
import os
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])



class MainPage(webapp2.RequestHandler):

    def get(self):

	tracks = {}

	with open('tracks2', 'r') as file:
		for line in file:
			newDic = {}
			for token in line.split(','):
				if (len(token) > 1):
 					name, value = token.split('#', 1)
 					newDic[name] = value
			sessionName = newDic['session'].rstrip()

			if not (sessionName in tracks.keys()):
				tracks[sessionName] = [newDic]
			else:
				tracks[sessionName].append(newDic)
        
        template_values = {
            'tracks':tracks,
            'Title': "The Alan Lomax Player"
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)