# here we treat this definition as a module
# only works because of the __init__.py file 
# there is no code there but its presence help import files among files

from app.shopping import format_usd

def test_format_usd():
    assert format_usd(9.5) == "$9.50"
