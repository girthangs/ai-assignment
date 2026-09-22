from cart import Cart

def test_total():
    c = Cart()
    c.add_item("apple", 1.00, 3)
    c.add_item("bread", 2.50, 1)
    assert c.total() == 5.50

def test_discount():
    c = Cart()
    c.add_item("apple", 1.00, 10)
    assert c.apply_discount(10) == 9.00

def test_remove_item():
    c = Cart()
    c.add_item("apple", 1.00, 1)
    c.add_item("banana", 0.50, 1)
    c.remove_item("apple")
    assert len(c.items) == 1
    assert c.items[0]["name"] == "banana"