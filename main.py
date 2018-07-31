
import webapp2
import os
import random
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from models import Item, UserAccount

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

        welcome_template = jinja_current_directory.get_template('/htmls/mainpage.html')
        self.response.write(welcome_template.render({'greeting': greeting}))

class AccountHandler(webapp2.RequestHandler):
    def get(self):
        logout_link = users.create_logout_url('/')
        account_template = jinja_current_directory.get_template('/htmls/account.html')
        self.response.write(account_template.render({'logout_link': logout_link}))

class ProductsHandler(webapp2.RequestHandler):
    def get(self):
        products_template = jinja_current_directory.get_template('/htmls/cur_products.html')
        self.response.write(products_template.render())

<<<<<<< HEAD
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
=======
class ListsHandler(webapp2.RequestHandler):
    def get(self):
        lists_template = jinja_current_directory.get_template('/htmls/lists.html')
        self.response.write(lists_template.render())

class InventoryHandler(webapp2.RequestHandler):
    def get(self):
        inventory_template = jinja_current_directory.get_template('/htmls/inventory_input.html')
        self.response.write(inventory_template.render())
>>>>>>> NewBranch


app = webapp2.WSGIApplication([
    ('/', HelloHandler),
    ('/account', AccountHandler),
    ('/inventory-input', InventoryHandler),
    ('/products', ProductsHandler),
    ('/lists', ListsHandler)
], debug=True)
