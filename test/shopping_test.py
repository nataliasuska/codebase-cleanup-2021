# here we treat this definition as a module
# only works because of the __init__.py file 
# there is no code there but its presence help import files among files

import os
from pandas import read_csv
from app.shopping import format_usd, lookup_product

def test_format_usd():
    assert format_usd(9.5) == "$9.50"
    


# this section is from https://github.com/s2t2/codebase-cleanup-2021/pull/5/commits/26b96b5ca7ac0217a5c71e9c0f85578af3c38d03
# consider making this a fixture!
mock_products_filepath = os.path.join(os.path.dirname(__file__), "mock_data", "mock_products.csv")
mock_products_df = read_csv(mock_products_filepath)
mock_products = mock_products_df.to_dict("records")

def test_lookups():
    # with valid product id, returns the product info:
    valid_result = lookup_product("8", mock_products)
    assert valid_result == {
        'aisle': 'Aisle C',
        'department': 'snacks',
        'id': 8,
        'name': 'Product 8',
        'price': 10.0
    }
    # with invalid product id, returns None:
    invalid_result = lookup_product("88888888", mock_products)
    assert invalid_result == None
