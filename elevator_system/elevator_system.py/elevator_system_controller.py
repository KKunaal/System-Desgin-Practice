from models import ElevatorController, ExternalPanel
from models.enums import floor_numbers

class ElevatorSystemController:
    def __init__(self, external_panels: list[ExternalPanel], elevator_controllers: list[ElevatorController]):
        self.external_panels = external_panels
        self.elevator_controllers = elevator_controllers

    
    def submitFloorRequest(self, floor):
        for external_panel in self.external_panels:
            if external_panel.floor == floor:
                external_panel.elevator_choosing_strategy.Choose(self.elevator_controllers)
    
    def submitInternalRequest(self, specific_elevator_controller: ElevatorController, floor):
        for ekevator_controller in self.elevator_controllers:
            if ekevator_controller.elevator == specific_elevator_controller.elevator:
                required_elevator_controller = ekevator_controller
                break
    
        if required_elevator_controller.elevator.current_floor >= floor:
            required_elevator_controller.up_requests.append(floor)
        if required_elevator_controller.elevator.current_floor < floor:
            required_elevator_controller.down_requests.append(floor)
        
        required_elevator_controller.elevator_moving_strategy.Move()