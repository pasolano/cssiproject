class UserAccount(ndb.Model):
    user_id = ndb.StringProperty(required=True)

class Item(ndb.Model):
    owner = ndb.StringProperty(required=True)
    product_name = ndb.StringProperty(required=True)
    expiration_date = ndb.DateTimeProperty(required=True)
