from calculator import square


def test_normal():
    assert square(4) == 16
    assert square(5) == 25

def test_one():
    assert square(1) == 1
    
def test_two():
    assert square(2) == 4
        
