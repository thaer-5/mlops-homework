from app.feature_engineering import hash_feature

def test_feature_consistency():
    value = "user123"
    result1 = hash_feature(value)
    result2 = hash_feature(value)
    assert result1 == result2
