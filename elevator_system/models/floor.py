from models.elevator import Elevator
from models.panel import Panel
from strategies.elevator_choosing_strategy import ElevatorChoosingStrategy

class Floor:
    def __init__(self, elevators: list[Elevator], external_panel):
        self.elevators = elevators
        self.external_panel = external_panel


class ExternalPanel(Panel):
    def __init__(self, floor: Floor,elevator_choosing_strategy: ElevatorChoosingStrategy):
        self.floor = floor
        self.elevator_choosing_strategy = elevator_choosing_strategy

class ExternalPanelController:
    def __init__(self):
        pass