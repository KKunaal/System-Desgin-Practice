

class FlightInstance:

    def __init__(self, source_airport, destination_airport, departure_date_time):
        self.source_airport = source_airport
        self.destination_airport = destination_airport
        self.departure_date_time = departure_date_time
        self.airline = ""
        self.flight_number = ""
        self.available_seats = 0
        self.price_per_seat = 0