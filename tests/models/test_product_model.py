import sys
sys.path.append('.')
from models.base_model import BaseModel
from models.product import Product


name = 'Test'
description = 'description'
price = 350

product = Product(name, description, price)

def test_compare_column_model():
    assert product.name == name
    assert product.description == description


def test_compare_type_column_model():
    assert type(product.name) == str
    assert type(product.description) == str
    assert type(product.price) == float


def test_compare_isinstance():
    assert isinstance(product, BaseModel)
    assert isinstance(product, Product)


def test_has_attribute():
    assert hasattr(product, 'name')
    assert hasattr(product, 'description')
    assert hasattr(product, 'price')

def test_validate_name():
    try:
        Product(' ', 'test test test',7.3)
    except Exception as e:
        assert isinstance(e, ValueError)


def test_validate_description():
    try:
        Product('Test', 'teste'*400, 4.1)
    except Exception as e:
        assert isinstance(e, ValueError)

def test_validate_price():
    try:
        Product('ssss', 'test test test','7,3')
    except Exception as e:
        assert isinstance(e, ValueError)
