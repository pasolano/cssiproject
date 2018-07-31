from google.appengine.ext import ndb

class UserAccount(ndb.Model):
    user_id = ndb.StringProperty(required=True)

class Item(ndb.Model):
    owner = ndb.StringProperty(required=True)
    item_name = ndb.StringProperty(required=True)
    expiration_date = ndb.DateTimeProperty(required=True)