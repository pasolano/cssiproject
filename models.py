from google.appengine.ext import ndb
from google.appengine.api import users

class Item(ndb.Model):
    user_id = ndb.StringProperty(required=True)
    item_name = ndb.StringProperty(required=True)
    expiration_date = ndb.StringProperty(required=True)
    use_time = ndb.StringProperty(required=True)

    @classmethod
    def get_by_user(cls, user):
        return cls.query().filter(cls.user_id == user.user_id()).fetch()
