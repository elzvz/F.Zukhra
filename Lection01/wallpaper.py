def calculate_number_or_roll_of_wallpapers (lenght_of_the_room, width_of_the_room, width_of_wallpaper, length_of_wallpaper ,ceiling_height):

    """
    >>> calculate_number_or_roll_of_wallpapers(5,6,1.06,10,2.75)
    7

    :param lenght_of_the_room:
    :param width_of_the_room:
    :param width_of_wallpaper:
    :param length_of_wallpaper:
    :param ceiling_height:
    :return:
    """
    number_or_roll_of_wallpapers =round ((round((lenght_of_the_room + width_of_the_room)*2/width_of_wallpaper))/(int (length_of_wallpaper/(ceiling_height+0.1))))
    return number_or_roll_of_wallpapers
print(calculate_number_or_roll_of_wallpapers(5,6,1.06,10,2.75))
print(calculate_number_or_roll_of_wallpapers(4,7,2,12,3))
print(calculate_number_or_roll_of_wallpapers(4,4,2,10,3))
print(calculate_number_or_roll_of_wallpapers(3,4,2,12,2.5))
