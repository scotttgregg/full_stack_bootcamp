# # unit_converter

distance = float(input("What is the distance?\n"))
input_unit = input("What is the unit?\n")
output_unit = input("what is the output unit?\n")


def feet_to_meters():
    return distance * .0348

def km_to_meters():
    return distance * 1000

def mi_to_meters():
    return distance * 1609.34

def m_to_feet():
    return distance * 3.28084

def km_to_feet():
    return distance * 3280.84

def mi_to_feet():
    return distance * 5280

def ft_to_km():
    return distance * .0003048

def m_to_km():
    return distance * .001

def mi_to_km():
    return distance * 1.60934

def ft_to_mi():
    return distance * .000189394

def m_to_mi():
    return distance * .000621371

def km_to_mi():
    return distance * .621371


if input_unit == "ft" and output_unit == "m":
    print(feet_to_meters())
elif input_unit == "km" and output_unit == "m":
    print(km_to_meters())
elif input_unit == "mi" and output_unit == "m":
    print(mi_to_meters())
elif input_unit == output_unit:
    print(distance + output_unit)
elif input_unit == "m" and output_unit == "ft":
    print(m_to_feet())
elif input_unit == "km" and output_unit == "ft":
    print(km_to_feet())
elif input_unit == "mi" and output_unit == "ft":
    print(mi_to_feet())
elif input_unit == "ft" and output_unit == "km":
    print(ft_to_km())
elif input_unit == "m" and output_unit == "km":
    print(m_to_km())
elif input_unit == "mi" and output_unit == "km":
    print(mi_to_km())
elif input_unit == "ft" and output_unit == "mi":
    print(ft_to_mi())
elif input_unit == "km" and output_unit == "mi":
    print(km_to_mi())
elif input_unit == "m" and output_unit == "mi":
    print(m_to_mi())
