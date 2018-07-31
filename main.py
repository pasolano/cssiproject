
import webapp2
import os
import random
import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb
from models import Item

# from google.appengine.ext import ndb
# from google.appengine.api import users

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def get_item_name(statement):
    return statement

def get_expiration_date(statement):
    return statement

class HelloHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            logout_url = users.create_logout_url('/')
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' % (nickname, logout_url))
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="%s">Sign in</a>' % (login_url)
        user.user_id()

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

    def post(self):
        user = users.get_current_user()
        template_product = self.request.get('product_name')
        template_expiration_date=Template.query(Template.name==template_product).fetch(1)[0].key
        item = {
            #'owner' = user
            'product_name': get_item_name(self.request.get('item_name')),
            'expiration_date': get_expiration_date(self.request.get('expiration_date')),
        }
        inventory_template = JINJA_ENVIRONMENT.get_template('templates/inventory_table.html')
        self.response.write(inventory_template.render(item))

# user.user_id()
#
# class Event (ndb.Model):
#     organizer=ndb.StringProperty(required=True)
#     title=ndb.StringProperty(required=True)
#
# Event(organizer=user.user_id(), title="LISTener")

app = webapp2.WSGIApplication([
    ('/', HelloHandler),
    ('/account', AccountHandler),
    ('/inventory_input', InventoryHandler)
], debug=True)
