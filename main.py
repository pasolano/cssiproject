
import webapp2
import os
import random
import jinja2
from google.appengine.api import users


jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

user = users.get_current_user()
if user:
    nickname = user.nickname()
    logout_url = users.create_logout_url('/')
    greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
        nickname, logout_url)
else:
    login_url = users.create_login_url('/')
    greeting = '<a href="{}">Sign in</a>'.format(login_url)


class HelloHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_current_directory.get_template('/mainpage.html')
        self.response.write(welcome_template.render())

class AccountHandler(webapp2.RequestHandler):
    def get(self):
        account_template = jinja_current_directory.get_template('/account.html')
        self.response.write(account_template.render())

class InventoryHandler(webapp2.RequestHandler):
    def get(self):
        inventory_template = jinja_current_directory.get_template('/inventory_input.html')
        self.response.write(inventory_template.render())


app = webapp2.WSGIApplication([
    ('/', HelloHandler),
    ('/account', AccountHandler),
    ('/inventory-input', InventoryHandler)
], debug=True)
