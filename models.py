from google.appengine.ext import ndb
from google.appengine.api import users

class Item(ndb.Model):
    user_id = ndb.StringProperty(required=True)
    item_name = ndb.StringProperty(required=True)
<<<<<<< HEAD
    expiration_date = ndb.DateProperty(required=True)
    use_time = ndb.StringProperty(required=True)
=======
    expiration_date = ndb.StringProperty(required=True)
    use_time = ndb.StringProperty(required=True, default="")
>>>>>>> 38806029f6d298613500f598ad5b69fe48c65ca5
    is_in_list = False

    @classmethod
    def get_by_user(cls, user):
        return cls.query().filter(cls.user_id == user.user_id()).fetch()

    @classmethod
    def expired_by_user(cls, user, date):
        return cls.query().filter(cls.user_id == user.user_id(), cls.expiration_date < date).fetch()

class ShoppingListItem(ndb.Model):
    user_id = ndb.StringProperty(required=True)
    item = ndb.KeyProperty(Item)

    @classmethod
    def get_by_user(cls, user):
        return cls.query().filter(cls.user_id == user.user_id()).fetch()

#if want multiple lists for one user, would want to make a new class model
