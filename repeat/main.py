import webapp2
from google.appengine.api import urlfetch

class HelloWorld(webapp2.RequestHandler):
    def get(self):
        message = self.request.get("message")

        if not message:
            serviceResponse = urlfetch.fetch(self.request.host_url+"/hello/v1/service", follow_redirects=False);
            message = serviceResponse.content

        self.response.write(message.title())
        self.response.status_int = 200

app = webapp2.WSGIApplication([
    ('/repeat/v1/service', HelloWorld)
], debug=True)
