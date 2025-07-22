

class OldPrinter:
    def make_copy(self):
        print("Printing using old printer")

class NewPrinterInterface:
    def print_document(self):
        raise NotImplementedError("Subclasses must implement this method!")

class NewPrinterBackOffice(NewPrinterInterface):
    def print_document(self):
        print("Printing using new interface !!")


class Adapter(NewPrinterInterface):
    def __init__(self, old_printer: OldPrinter):
        self.old_printer = old_printer
    
    def print_document(self):
        self.old_printer.make_copy()

new_printer = NewPrinterBackOffice()
new_printer.print_document()

old_printer = OldPrinter()
adapter = Adapter(old_printer)
adapter.print_document()



'''
Summary: 
Adapter is one which lets use use new methods with a old class
or access old APIS with new interfaces
'''
