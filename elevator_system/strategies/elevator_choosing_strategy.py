from models.elevator import ElevatorController

class ElevatorChoosingStrategy:
    def __init__(self, elevator_controllers: list[ElevatorController]):
        self.elevator_controllers = elevator_controllers

    def Choose(self, floor):
        ## whichever elevator is moving towards the given floor and has minimum up_requests should come on that floor
        self.elevator_controllers[0].down_requests.append(floor)
        self.elevator_controllers[0].move()
        return self.elevator_controllers[0]