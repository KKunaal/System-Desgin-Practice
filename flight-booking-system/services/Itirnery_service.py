from services.flight_instance import FlightInstance

class ItirneryService:

    def __init__(self, flight_instances: list[FlightInstance], ticket_count):
        self.flight_instances = flight_instances
        self.ticket_count = ticket_count

    def get_itirnery_price(self):
        price = 0
        for flight_instance in self.flight_instances:
            price = price + flight_instance.price_per_seat

        return price*self.ticket_count
