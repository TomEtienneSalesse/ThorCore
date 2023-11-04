import periodictable
from scipy.constants import find, physical_constants
from periodictable import *

class Elements:
    
    def get_element_info_by_symbol(symbol):
        element = periodictable.elements.symbol(symbol)
        
        element_data = {
            "name": element.name,
            "symbol": element.symbol,
            "number": element.number,
            "mass": element.mass,
            "density": element.density,
            "isotopes": element.isotopes,
            "charge":element.charge,
            "ions":element.ions,
        }
        
        return element_data
    
    def get_table():
        table=[{
            "name": None,
            "symbol": None,
            "number": None,
            "mass": None,
            "density": None,
            "isotopes": None,
            "charge":None,
            "ions":None,
        }]
        for element in periodictable.elements:
            if str(element) != "n":
                table.append(Elements.get_element_info_by_symbol(str(element)))
        return table
    
class Values:

    def get_constants():
        constants_info = []

        for constant in find():
            value, unit, symbol = physical_constants[constant]
            constants_info.append({
                "name": constant,
                "value": value,
            })

        return constants_info
    
    all_constants = get_constants()

    def get_value_from_dict(constant):
        for entry in Values.all_constants:
            if entry["name"] == constant:
                return entry["value"]
        return None

