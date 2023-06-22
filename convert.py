def celsius_to_farenheit(celsius):
    farenheit = celsius/5*9 + 32
    return farenheit

def celsius_to_kelvin (celsius):
    return celsius + 273.15
    
def kelvin_to_farenheit (kelvin):
    celsius = kelvin - 273.15
    return celsius_to_farenheit(celsius)