from daos.base_dao import BaseDao
from models.product import Product


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__(Product)
