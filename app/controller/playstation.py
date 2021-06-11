from fuzzywuzzy import fuzz


class ControllerPlaystation(object):
    __list_products = []

    @classmethod
    def save(cls, name, price, link, store):
        cls.__list_products.append({"price": price,
                                  "name": name,
                                  "link": link,
                                  "store": store})

    @classmethod
    def getter_products(cls):
        return cls.__list_products

    @classmethod
    def getter_products_fuzzy(cls):
        return [list for list in cls.__list_products if fuzz.ratio("Console Playstation 5", list['name']) > 50]


