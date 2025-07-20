from models import Floor, Elevator

class Building:
    def __init__(self, floors: list[Floor], elevators: list[Elevator]):
        self.floors = floors
        self.elevators = elevators