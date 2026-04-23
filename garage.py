def enter_garage(garage, car_id, entry_hour):
    if len(garage["cars"]) >= garage["capacity"]:
        raise ValueError("Garage is full")
    if car_id in garage["cars"].keys():
        raise ValueError("Car already in garage")
    if not isinstance(entry_hour, int):
        raise TypeError("Time must be numeric hour")

    garage["cars"][car_id] = entry_hour


def exit_garage(garage, car_id):
    garage["cars"].pop(car_id)


def get_available_spots(garage):
    pass


def calculate_fee(hours, rate):
    pass
