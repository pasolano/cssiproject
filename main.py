
import webapp2
import os
import random
import jinja2



jinja_current_directory = jinja2.Environment(

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



class HelloHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_current_directory.get_template('/mainpage.html')
        self.response.write(welcome_template.render())

class AccountHandler(webapp2.RequestHandler):
    def get(self):
        account_template = jinja_current_directory.get_template('/account.html')
        self.response.write(account_template.render())


app = webapp2.WSGIApplication([
    ('/', HelloHandler),
    ('/account', AccountHandler)
], debug=True)
