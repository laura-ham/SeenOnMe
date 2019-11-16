from google.appengine.ext import ndb

# class Review(ndb.Model):
#     description = ndb.StringProperty(indexed=False)
#     rating =  ndb.IntegerProperty(indexed=False)
#     # image = ndb.BlobProperty()
#     image = ndb.StringProperty(indexed=False)

# class User(ndb.Model):
#     height = ndb.FloatProperty(indexed=True)
#     waist = ndb.FloatProperty(indexed=True)
#     size = ndb.FloatProperty(indexed=True)

class Review(ndb.Model):
    product_id = ndb.StringProperty(indexed=True)
    merchant_id = ndb.StringProperty(indexed=True)
    order_id = ndb.StringProperty(indexed=True)
    timestamp = ndb.StringProperty(indexed=False)
    supplier_id = ndb.IntegerProperty(indexed=True)
    
    #user = ndb.StringProperty(indexed=False)
    #review = ndb.StringProperty(indexed=False)

    height = ndb.FloatProperty(indexed=True)
    waist = ndb.FloatProperty(indexed=True)
    size = ndb.FloatProperty(indexed=True)

    description = ndb.StringProperty(indexed=False)
    rating =  ndb.IntegerProperty(indexed=False)
    image = ndb.BlobProperty(indexed=False)

    verified = ndb.StringProperty(indexed=False)

class ToReview(ndb.Model):
    product_id = ndb.StringProperty(indexed=True)
    order_id = ndb.StringProperty(indexed=True)


class Datastore:
    def get_to_review(self, product_id, order_id):
        return ToReview.query(ToReview.order_id == order_id, ToReview.product_id == product_id).fetch()

    def add_to_review(self, product_id, order_id):
        entity = ToReview(product_id=product_id, order_id=order_id)
        entity.put()

    def add_review(self,
        product_id,
        merchant_id,
        order_id,
        height,
        waist,
        size,
        desc,
        rating,
        image,
        supplier_id):

        # review = Review(description = desc, rating = rating, image = image)
        # review.put()

        # user = User(height = height, waist=waist, size=size)
        # user.put()

        review = Review(product_id=product_id, merchant_id=merchant_id, order_id=order_id, timestamp="dd-mm-yyy", supplier_id=supplier_id, description = desc, rating = rating, image = image, height = height, waist=waist, size=size)
        review.put()

        # remove from ToReview list
        # entity = self.get_to_review(product_id=product_id, order_id=order_id)
        # entity.delete()

        # exists = self.check_entity_exists(entity)
        # if not exists:
        #     reg.put()
        #     return True
        # else:
        #     return False

    def verify_ids(self,
        product_id,
        order_id):

        # Check if entity is in Entity
        check = ToReview.query(ToReview.product_id == product_id, ToReview.order_id == order_id).fetch()
        if len(check) > 0:
            return True
        return False        

    def get_order_id(self, order_id):
        return Review.query(Review.order_id == order_id).fetch()

    def get_product_id(self, product_id):
        return Review.query(Review.product_id == product_id).fetch()

    # def check_registry_exists(self, registry):
    #     check = Registry.query(Registry.value == registry).fetch()
    #     if len(check) > 0:
    #         return True
    #     return False
