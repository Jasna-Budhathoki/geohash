from backend.geohash_decoder import decode


def test_decode_1():
    assert decode("tv5b1k4c") == {
        "latitude": 28.14723014831543,
        "longitude": 84.08231735229492,
    }


def test_decode_2():
    assert decode("tv58xm8n") == {
        "latitude": 28.244218826293945,
        "longitude": 83.99065017700195,
    }


def test_decode_3():
    assert decode("tv58x1eu") == {
        "latitude": 28.22190284729004,
        "longitude": 83.98481369018555,
    }
