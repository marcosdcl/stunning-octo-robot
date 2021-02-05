import re
from sqlalchemy import Column, String, Numeric
from models.base_model import BaseModel
from sqlalchemy.orm import validates

class Product(BaseModel):
    __tablename__ = 'product_group03'
    name = Column(String(length=150), nullable=False)
    description = Column(String(length=200), nullable=True)
    price = Column(Numeric, nullable=False)

    @validates('name')
    def validate_name(self, key, name):
        if name is None:
            raise ValueError("Please write a name!")
        elif name.strip(' ') == '':
            raise ValueError("Name can't be null!")
        return name
    
    @validates('description')
    def validate_description(self, key, description):
        if len(description) > 300:
            raise ValueError("Please, a description has exceeded the 300 character limit!")
        return description

    @validates('price')
    def validate_price(self,key,price):
        if re.search('[a-zA-Z,]',str(price)):
           raise ValueError("Price can't have a character!")
        return float(price) 

    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price
