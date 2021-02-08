from resources.base_resource import BaseResource
from daos.product_dao import ProductDao
from models.product import Product
from flask_restful import fields, marshal_with


class ProductResource(BaseResource):
    fields = {
        'id_': fields.Integer,
        'name': fields.String,
        'description': fields.String,
        'price': fields.Float
    }

    def __init__(self) -> None:
        self.__dao = ProductDao()
        self.__model_type = Product
        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def get(self, id = None):
        return super().get(id)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self):
        return super().put()

    @marshal_with(fields)
    def delete(self, id):
        return super().delete(id)