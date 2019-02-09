petrol_filling_in_liter = int(input('Сколько литров бензина заправили? '))
print(petrol_filling_in_liter)
print (type(petrol_filling_in_liter))

drive_on_this_petrol = int(input('Сколько км проехали после заправки? '))
print(drive_on_this_petrol)
print(type(drive_on_this_petrol))
petrol_consumption_in_litre_per_100_km = petrol_filling_in_liter/drive_on_this_petrol*100
print(petrol_consumption_in_litre_per_100_km)
petrol_volume = int (input('Сколько бензина в баке? '))


def  calculate_max_distance_on_this_petrol (petrol_volume, petrol_consumption_in_litre_per_100_km):
    """
    >>> calculate_max_distance_on_this_petrol(10,5)
    200.0

    :param petrol_volume:
    :param petrol_consumption_in_litre_per_100_km:
    :return:
    """
    result = petrol_volume * 100 / petrol_consumption_in_litre_per_100_km
    return result
print(calculate_max_distance_on_this_petrol(10, 5))

