
class OldApi:
    def get_response(self):
        print("getting responses using old API !!")

class NewAPI:
    def fetch_data(self):
        raise NotImplementedError("This method needs to be implemented in subclasses !")
    
class NewAPIBackOffice(NewAPI):
    def fetch_data(self):
        print("Fetching data using new API !!")

class Adapter(NewAPI):
    def __init__(self, old_api: OldApi):
        self.old_api = old_api

    def fetch_data(self):
        self.old_api.get_response()

A = NewAPIBackOffice()
A.fetch_data()

B = OldApi()
AdapterB = Adapter(B)
AdapterB.fetch_data() 