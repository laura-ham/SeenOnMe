# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
from store import Datastore

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

class Test(webapp2.RequestHandler):
    def get(self):
        q = self.request.get('q')

        datastore = Datastore()
        something =  datastore.get_product_id(q)

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(str(something))

class Upload(webapp2.RequestHandler):
    def put(self):
        product_id = self.request.get('product_id')
        merchant_id = self.request.get('merchant_id')
        order_id = self.request.get('order_id')
        height = self.request.get('height')
        waist = self.request.get('waist')
        size = self.request.get('size')
        desc = self.request.get('desc')
        rating = self.request.get('rating')
        supplier_id = self.request.get('supplier_id')

        uploaded_file = self.request.POST.get('image')
        image = uploaded_file.file.read()

        datastore = Datastore()

        datastore.add_entity(
            product_id = product_id,
            merchant_id = merchant_id,
            order_id = order_id,
            height = float(height),
            waist = float(waist),
            size = float(size),
            desc = desc,
            rating = int(rating),
            image = image,
            supplier_id = int(supplier_id)
        )

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Entity Added')

class Verify(webapp2.RequestHandler):
    def get(self):
        product_id = self.request.get('product_id')
        merchant_id = self.request.get('merchant_id')
        order_id = self.request.get('order_id')
        supplier_id = self.request.get('supplier_id')

        datastore = Datastore()

        verified = datastore.verify_ids(
            product_id = product_id,
            merchant_id = merchant_id,
            order_id = order_id,
            supplier_id = int(supplier_id)
        )

        self.response.headers['Content-Type'] = 'text/plain'
        if verified: 
            self.response.write('Ids verified')
        else:
            self.response.write('ERROR')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/upload', Upload),
    ('/verify', Verify),
    ('/test', Test)
], debug=True)
