

class Alert(object):
    def __init__(self, user, price_limit, item):
        self.user = user
        self.price = price_limit
        self.item = item

    def __repr__(self):
        return "<Alerts for {} on item {} with price {}>".format(self.user.email, self.item.name, self.price_limit)
