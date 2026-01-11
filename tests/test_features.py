from app.feature_engineering import hash_feature

def test_hash_feature_known_value():
    result = hash_feature("hello", 100)
    assert isinstance(result, int)
    assert 0 <= result < 100
