from backend.geohash_encoder import encode

def test_encode_1():
    """geohash encode converts latitude of 27.7340 and longitude of 85.3368 to 'tuutvbu6'. """
    assert encode(27.7340,85.3368) == 'tuutvbu6'

def test_encode_2():
    """geohash encode converts latitude of -78.4568 and longitude of 88.5637 to 'jfncxm6h'."""
    assert encode(-78.4568,88.5637) == 'jfncxm6h'

def test_encode_3():
    """geohash encode converts latitude of 27.7775 and longitude of 85.3686 to 'tuuwn8ex'."""
    assert encode(27.7775,85.3686) == 'tuuwn8ex'

    
