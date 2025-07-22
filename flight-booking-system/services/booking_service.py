import uuid

class BookingService:

    def __init__(self, itirnery, payment_service):
        self.id = uuid.uuid4()
        self.itirnery = itirnery
        self.payment_service = payment_service
        self.payment_status = "PENDING"
        self.payment_id = ""
        self.booking_status = "PENDING"
        self.booking_id = ""

    def book_itirnery(self):
        self.payment_service.make_payment()
    