from flask import Flask
from flask_restful import Api
from resources.product_resource import ProductResource


app = Flask(__name__)
api = Api(app)

api.add_resource(ProductResource, '/product', endpoint = 'products')
api.add_resource(ProductResource, '/product/<int:id>', endpoint = 'product')

app.run(debug = True)
