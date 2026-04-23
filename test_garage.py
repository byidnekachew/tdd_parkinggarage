from garage import enter_garage

def test_enter_garage_works():
    garage_dict = {"capacity": 10, "cars": {}}
    enter_garage(garage_dict, "ABC1234", 13)
    assert "ABC1234" in garage_dict["cars"].keys()

def test_enter_garage_valerr_if_full():
    with pytest.raises(ValueError):
        garage_dict = {"capacity": 1, "cars": {"ABC1234": 13}}
        enter_garage(garage_dict, "XYZ5678", 15)