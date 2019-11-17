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
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

class Test(webapp2.RequestHandler):
    def get(self):
        q = self.request.get('q')

        datastore = Datastore()
        something =  datastore.get_product_id(q)

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write( json.dumps( {'data': str(something)} ) )

class Upload(webapp2.RequestHandler):
    def put(self):
        jsonstring = self.request.body
        jsonstring = jsonstring.replace("'", '"')
        jsonobject = json.loads(jsonstring)

        product_id = jsonobject['product_id']
        merchant_id = jsonobject['merchant_id']
        order_id = jsonobject['order_id']
        height = jsonobject['height']
        waist = jsonobject['waist']
        size = jsonobject['size']
        desc = jsonobject['desc']
        image = jsonobject['image']
        rating = jsonobject['rating']
        supplier_id = jsonobject['supplier_id']

        # uploaded_file = self.request.POST.get('image')
        # image = uploaded_file.file.read()

        # img_url = imagecloud.upload_image(image, order_id + ":" + merchant_id)

        datastore = Datastore()
            

        try:
            datastore.add_review(
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

            self.response.headers['Content-Type'] = 'application/json'
            self.response.write( json.dumps( {'data': {'code': 201, 'message': "Successful lalalala"}	}) )

        except Exception as e:
            self.response.headers['Content-Type'] = 'application/json'
            self.response.write( json.dumps( {'data': {'code': 500, 'message': e.message}	}) )

class Verify(webapp2.RequestHandler):
    def get(self):
        product_id = self.request.get('product_id')
        order_id = self.request.get('order_id')

        datastore = Datastore()

        try:
            verified = datastore.verify_ids(
                product_id = product_id,
                order_id = order_id
            )

            self.response.headers['Content-Type'] = 'application/json'
            if verified: 
                self.response.write( json.dumps( {'data': {'code': 201, 'message': "Ids Verified"}	}) )
            else:
                self.response.write( json.dumps( {'data': {'code': 404, 'message': "not found in database"}	}) )

        except Exception as e:
            self.response.write( json.dumps( {'data': {'code': 500, 'message': e.message}	}) )

class Register(webapp2.RequestHandler):
    def put(self):
        jsonstring = self.request.body
        jsonstring = jsonstring.replace("'", '"')
        jsonobject = json.loads(jsonstring)
        product_id = jsonobject['product_id']
        order_id = jsonobject['order_id']

        datastore = Datastore()

        try:
            datastore.add_to_review(
                product_id = product_id,
                order_id = order_id,
            )

            self.response.headers['Content-Type'] = 'application/json'
            self.response.write( json.dumps( {'data': {'code': 201, 'message': "Data Successfully Added"}	}) )
        
        except Exception as e:
            self.response.headers['Content-Type'] = 'application/json'
            self.response.write( json.dumps( {'data': {'code': 500, 'message': e.message}	}) )

class Reviews(webapp2.RequestHandler):
    def get(self):

        merchant_id = self.request.get('merchant_id')
        height = self.request.get('height')
        waist = self.request.get('waist')
        size = self.request.get('size')
        
        datastore = Datastore()

        try:
            if len(size) > 0:
                size = float(size)
            else:
                size = None

            if len(height) > 0:
                height = float(height)
            else:
                height = None

            if len(waist) > 0:
                waist = float(waist)
            else:
                waist = None

        
            reviews = datastore.get_reviews(
                merchant_id = merchant_id,
                height = height,
                waist = waist,
                size = size
                )

            data = []
            for rev in reviews:
                dataDict = dict()
                dataDict['height'] = rev.height
                dataDict['waist'] = rev.waist
                dataDict['size'] = rev.size
                dataDict['rating'] = rev.rating
                dataDict['description'] = rev.description
                dataDict['image'] = rev.image

                data.append(dataDict)

            jData = json.dumps( {'data': data } )

            self.response.headers['Content-Type'] = 'application/json'
            self.response.write(jData)
        
        except Exception as e:
            self.response.headers['Content-Type'] = 'application/json'
            self.response.write( json.dumps( {'data': {'code': 500, 'message': e.message}	}) )

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/upload', Upload),
    ('/verify', Verify),
    ('/register', Register),
    ('/test', Test),
    ('/reviews', Reviews)
], debug=True)
