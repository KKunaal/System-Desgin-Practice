from models import Panel
from enums import floor_numbers
from strategies import ElevatorMovementStrategy

class InternalPanel(Panel):
    def __init__(self, buttons: list, preseed: list):
        self.buttons = buttons
        self.preseed = preseed

class Elevator:
    def __init__(self, floor: int, direction, internal_panel: InternalPanel, state):
        self.current_floor = floor
        self.direction = direction
        self.panel = internal_panel
        self.state = state

class ElevatorController:
    def __init__(self, elevator: Elevator, up_requests: list, down_requests: list, elevator_moving_strategy: ElevatorMovementStrategy):
        self.elevator = elevator
        self.up_requests = up_requests
        self.down_requests = down_requests
        self.elevator_moving_strategy = elevator_moving_strategy

    def move(self):
        return self.elevator_moving_strategy.Move(self)
        