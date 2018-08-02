
import webapp2
import os
import random
import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from models import Item, ShoppingListItem
import datetime
import time



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
        welcome_template = jinja_current_directory.get_template('/htmls/mainpage.html')
        self.response.write(welcome_template.render())

class AccountHandler(webapp2.RequestHandler):
    def get(self):
        logout_link = users.create_logout_url('/')
        account_template = jinja_current_directory.get_template('/htmls/account2.html')
        self.response.write(account_template.render({'logout_link': logout_link}))

class ProductsHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        # Item(
        # item_name=self.request.get('item_name'),
        # expiration_date=self.request.get('expiration_date'),
        # use_time=self.request.get('use_time'),
        # user_id=user.user_id()
        # ).put()
        items = list(Item.get_by_user(user))
        inventory_template = jinja_current_directory.get_template('/htmls/cur_products.html')
        self.response.write(inventory_template.render(items=items))



class ListsHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        shopping_items = ShoppingListItem.get_by_user(user)
        names = []
        for list_item in shopping_items:
            names.append(list_item.item.get().item_name)
        # print(names)
        lists_template = jinja_current_directory.get_template('/htmls/lists.html')
        self.response.write(lists_template.render(names=names))

    # def post(self):

class AddItemHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        new_item = self.request.get("item_name")
        self.response.write("hello" + new_item)
        current_item = Item.query().filter(Item.item_name == new_item).get()
        ShoppingListItem(
        user_id=user.user_id(),
        item=current_item.key
        ).put()


        self.redirect('/lists')



class InventoryHandler(webapp2.RequestHandler):
    def get(self):
        inventory_template = jinja_current_directory.get_template('/htmls/inventory_input.html')
        self.response.write(inventory_template.render())
    def post(self):
        user = users.get_current_user()
        Item(
        item_name=self.request.get('item_name'),
        expiration_date=datetime.datetime.strptime(self.request.get('expiration_date'),"%Y-%m-%d").date(),
        use_time=self.request.get('use_time'),
        user_id=user.user_id()
        ).put()
        items = list(Item.get_by_user(user))
        inventory_template = jinja_current_directory.get_template('/htmls/inventory_input.html')
        self.response.write(inventory_template.render(items=items))

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        contact_template = jinja_current_directory.get_template('/htmls/contact.html')
        self.response.write(contact_template.render())

class NotificationHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        expired_items = list(Item.expired_by_user(user, datetime.datetime.now().date()))
        contact_template = jinja_current_directory.get_template('/htmls/notifications.html')
        self.response.write(contact_template.render(expired_items=expired_items))


class AboutHandler(webapp2.RequestHandler):
    def get(self):
        about_template = jinja_current_directory.get_template('/htmls/about.html')
        self.response.write(about_template.render())

class RedirectHomeHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("/")




app = webapp2.WSGIApplication([
    ('/', HelloHandler),
    ('/account', AccountHandler),
    ('/inventory-input', InventoryHandler),
    ('/cur_products', ProductsHandler),
    ('/lists', ListsHandler),
    ('/contact', ContactHandler),
    ('/add_item_to_list', AddItemHandler),
    ('/notifications', NotificationHandler),
    ('/about', AboutHandler),
    ('/.*', RedirectHomeHandler)
], debug=True)
