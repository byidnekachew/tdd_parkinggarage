import pytest
from garage import enter_garage, exit_garage, get_available_spots, calculate_fee

# Tests for enter_garage
def test_enter_garage_works():
    garage_dict = {"capacity": 10, "cars": {}}
    enter_garage(garage_dict, "ABC1234", 13)
    assert "ABC1234" in garage_dict["cars"].keys()


def test_enter_garage_valerr_if_full():
    with pytest.raises(ValueError):
        garage_dict = {"capacity": 1, "cars": {"ABC1234": 13}}
        enter_garage(garage_dict, "XYZ5678", 15)


def test_enter_garage_valerr_if_car_exists():
    with pytest.raises(ValueError):
        garage_dict = {"capacity": 10, "cars": {"ABC1234": 13}}
        enter_garage(garage_dict, "ABC1234", 15)


def test_enter_garage_typeerr_if_time_not_int():
    with pytest.raises(TypeError):
        garage_dict = {"capacity": 10, "cars": {}}
        enter_garage(garage_dict, "ABC1234", "three o'clock")


# Tests for exit_garage
def test_exit_garage_works():
    garage_dict = {"capacity": 10, "cars": {"ABC1234": 13}}
    exit_garage(garage_dict, "ABC1234")
    assert "ABC1234" not in garage_dict["cars"].keys()


def test_exit_garage_keyerr_if_car_not_exist():
        with pytest.raises(KeyError):
            garage_dict = {"capacity": 10, "cars": {}}
            exit_garage(garage_dict, "ABC1234")


# Tests for get_availible_spots
def test_get_available_spots_works():
    garage_dict = {"capacity": 10, "cars": {"ABC1234": 13}}
    assert get_available_spots(garage_dict) == 9


def test_get_available_spots_empty():
    garage_dict = {"capacity": 1, "cars": {"ABC1234": 13}}
    assert get_available_spots(garage_dict) == 0


# Tests for calculate_fee
@pytest.mark.parametrize("hours, rate, expected", [
    (3, 2, 6.00),
    (8, 2.5, 20.00),
    (5.5, 2, 11.00)
])
def test_calculate_fee_works(hours, expected):
    assert calculate_fee(hours, rate) == expected