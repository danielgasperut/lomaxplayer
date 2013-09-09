import jinja2
import os
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])



class MainPage(webapp2.RequestHandler):

    def get(self):

	sessions = []
	tracks = {}
	trackNo = 1

	#build the track/session list, this should be replaced with an object query.
	with open('tracks4', 'r') as file:
		for line in file:
			newDic = {}
			for token in line.rstrip().split(','):
				if (len(token) > 1):
 					name, value = token.split('#', 1)
 					if name == 'track':
 						value = trackNo
 					newDic[name] = value
			sessionName = newDic['session']
			trackNo = trackNo + 1
		
			if not (sessionName in sessions):
				sessions.append(sessionName)
				tracks[sessionName] = [newDic]
			else:
				#find the index in the order list
				tracks[sessionName].append(newDic)
			

		#renumber the tracks
					
		template_values = {
            'tracks':tracks,
            'sessions':sessions,
            'Title': "The Alan Lomax Player"
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)