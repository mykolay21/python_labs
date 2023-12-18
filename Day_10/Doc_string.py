

def format_name(f_name, l_name):
    """
     Take a first and last name
     :param f_name:
     :param l_name:
     :return:
     """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"


print(format_name("ANGELA", "YU"))
