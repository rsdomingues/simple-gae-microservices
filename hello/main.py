import webapp2

class HelloWorld(webapp2.RequestHandler):
	def get(self):
		self.response.write("Hello World!")
		self.response.status_int = 200

app = webapp2.WSGIApplication([
    ('/hello/v1/service', HelloWorld)
], debug=True)
