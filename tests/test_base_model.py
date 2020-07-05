from fifteen_five.models import BaseModel


def test_valid_args():
    BaseModel.valid_keys = ['key1']
    assert BaseModel.valid_args({'key1': 'val1', 'key2': 'val2'}) == {'key1': 'val1'}
