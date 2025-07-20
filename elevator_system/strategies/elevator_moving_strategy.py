from models.elevator import ElevatorController

class ElevatorMovementStrategy:
    def __init__(self, elevator_controller: ElevatorController):
        self.elevator_controller = elevator_controller

    def Move(self):
        if self.elevator_controller.elevator.direction == "UP":
                if self.elevator_controller.up_requests:
                    go_to_floor = self.elevator_controller.up_requests.pop()
                else:
                    go_to_floor = self.elevator_controller.down_requests.pop()
        if self.elevator_controller.elevator.direction == "DOWN":
                if self.elevator_controller.down_requests:
                    go_to_floor = self.elevator_controller.down_requests.pop()
                else:
                    go_to_floor = self.elevator_controller.down_requests.pop()   
            
        return go_to_floor