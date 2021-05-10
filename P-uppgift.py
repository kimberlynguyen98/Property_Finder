stripes = '______________________________________________________________________________________\n'


class Property:

    def __init__(self, price, area, rent, number, address):
        """
        :param price: Price of property (kr)
        :param area: Living space (kvm)
        :param rent: Monthly rent (kr)
        :param number: Phone number
        :param address: Address of property
        """
        self.price = price
        self.area = area
        self.rent = rent
        self.number = number
        self.address = address

    def __str__(self):
        return 'Price: ' + str(self.price) + '\nArea: ' + str(self.area) + '\nRent: ' + \
               str(self.rent) + '\nPhone number: ' + str(self.number) + '\nStreet address: ' + str(self.address)

    def monthly_cost(self, interest, deposit, deduction):
        """
        Function to calculate monthly cost
        :param self: Calculated on every apartment in list of properties. Also used to collect information from class
        :param interest: Interest from user input
        :param deposit: Deposit from user input
        :param deduction: Deduction from user input
        :return: Monthly cost of a an apartment
        """
        rent = int(self.rent)
        price = int(self.price)
        monthly_price = rent + (((price - deposit) * (interest / 100) * (1 - (deduction / 100))) / 12)
        return monthly_price

    def area_cost(self):
        """
        Function to calculate area cost
        :param self: Collects information from list with properties
        :return: Area cost of an apartment
        """
        price = int(self.price)
        area = float(self.area)
        area_price = price / area
        return area_price


def control_int(prompt_string):
    """
    Defining a function to use for error handling, used when user input are integers
    :param prompt_string: User input (integers), what's being controlled
    :return:
    """
    while True:
        try:
            number = int(input(prompt_string))
            if number < 0:
                raise ValueError
        except ValueError:
            print('\nIncorrect, please enter digits > 0\n')
        else:
            return number


def control_float(prompt_string):
    """
    Defining a function to use for error handling when user input are floats
    :param prompt_string: User input (float), what's being controlled
    :return:
    """
    while True:
        try:
            digit = float(input(prompt_string).replace(',', '.'))
            if digit < 0.0:
                raise ValueError
        except ValueError:
            print('\nIncorrect, please enter digits > 0.0!\n')
        else:
            return digit


def control_lower_letter(prompt_string):
    """
    Defining a function to use for error handling when user input are strings, wants lower case
    :param prompt_string: User input (strings), what's being controlled
    :return:
    """
    while True:
        try:
            letter = str(input(prompt_string))
            letter = letter.lower()
            if letter.lower() not in ('a', 'b', 'c', 'd'):
                raise IOError
        except IOError:
            print('\nIncorrect, please enter a, b, c or d!\n')
        else:
            return letter


def control_upper_letter(prompt_string):
    """
    Defining a function to use for error handling when user input are strings, wants upper case
    :param prompt_string: user input
    :return:
    """
    while True:
        try:
            upper_case = str(input(prompt_string))
            upper_case = upper_case.capitalize()
        except IOError:
            print('\nIncorrect, please enter letters!')
        else:
            return upper_case


def control_yes_no(prompt_string):
    """
    Defining a function to use for error handling when user input are strings, uppercase for Y or N answers
    :param prompt_string: user input
    :return:
    """
    while True:
        try:
            yes_no = str(input(prompt_string))
            yes_no = yes_no.capitalize()
            if yes_no.capitalize() not in ('Y', 'N'):
                raise IOError
        except IOError:
            print('\nIncorrect, please enter Y or N!\n')
        else:
            return yes_no


def read_properties_from_file(file_name):
    """
    Used to read properties from a file
    :param file_name: Input file to be read from
    :return: It returns with all properties on it
    """
    try:
        get_file = open(file_name, 'r')
        list_file = get_file.read()
        get_file.close()
        new_list = []
        for apartment in list_file.splitlines():
            values = []
            for attribute in apartment.split(','):
                values.append(attribute)
            if len(values) == 5:
                obj = Property(int(values[0]), float(values[1]), int(values[2]), values[3], values[4])
                new_list.append(obj)
            else:
                print('Error. The file is in the wrong format')
                quit()
    except IOError:
        print('Error. The file does not exist.')
        quit()
    else:
        return new_list


def read_settings_from_file(file_name):
    """
    Read settings from file, later used in the menu as choices to change
    :param file_name: Input file to be read from
    :return: Return one list of our settings
    """
    try:
        get_in_file = open(file_name, 'r')
        list_file = get_in_file.read()
        get_in_file.close()
        settings_list = list_file.split(',')
    except IOError:
        print('Error. The file does not exist.')
        quit()
    else:
        return settings_list


def save_settings_to_file(settings, file_name):
    """
    Save user inputs to file
    :param file_name: File to save to
    :param settings: Settings to be saved
    :return: None
    """
    with open(file_name, 'w+') as open_file:
        for item in settings:
            open_file.write(str(item) + ',')


def save_properties_to_file(properties, file_name):
    """
    Save properties to file
    :param file_name: File to save to
    :param properties: Properties to be saved
    :return:
    """
    with open(file_name, 'w+') as open_file:
        for item in properties:
            properties_list = '%s,%s,%s,%s,%s' % (item.price, item.area, item.rent, item.number, item.address)
            open_file.write(str(properties_list) + '\n')


def save_properties_to_print_file(print_property, file_name, interest, deposit, deduction):
    """
    Save properties to a new file for printout
    :param deduction: Deduction from user input
    :param deposit: Deposit from user input
    :param interest: Interest from user input
    :param file_name: File to save to
    :param print_property: Sorted properties
    :return:
    """
    with open(file_name, 'w+') as open_file:
        for x in print_property:
            monthly = x.monthly_cost(interest, deposit, deduction)
            area = x.area_cost()
            open_file.write(str(x.__str__()) + '\nMonthly cost: ' + str(monthly) + '\nArea cost: ' + str(area) +
                            '\n\n')


def menu(settings):
    """
    Prints out menu with changeable values from settings file
    :param settings: Takes parameter to define file to use
    :return: Prints out menu with setting values from a chosen file
    """
    print('\nYour options:')
    print(' 1 - Change desired monthly costs', '(<', settings[0], 'kr)\n', '2 - Change desired rent', '(<',
          settings[1], 'kr)\n', '3 - Change desired area cost', '(<', settings[2], 'kr)\n',

          '4 - Change desired living space', '(>', settings[3], 'kvm)\n', '5 - Create assortment\n',
          '6 - Sort by parameter\n', '7 - Add new property\n', '8 - Remove property\n', '9 - Exit')
    print(stripes)


def menu_choice():
    """
    User input for menu with error handling
    :return: Chosen option
    """
    while True:
        try:
            choice = control_int('Choose an option: ')
            if choice < 1 or choice > 9:
                raise ValueError
        except ValueError:
            print('\nPlease enter a number from 1-9!\n')
        else:
            return choice


def print_properties(properties, settings, interest, deposit, deduction):
    """
    Function used to print all properties that satisfies the users choice of monthly cost, rent etc.
    :param properties: Define file to use
    :param settings: Define file to use
    :param interest: User input
    :param deposit: User input
    :param deduction: User input
    :return: Filtrated list with properties
    """
    print_prop = []
    properties_exists = False
    for x in properties:
        monthly = x.monthly_cost(interest, deposit, deduction)
        area = x.area_cost()
        if monthly < int(settings[0]) and int(x.rent) < int(settings[1]) and area < float(settings[2]) and \
                float(x.area) > float(settings[3]):
            properties_exists = True
            print(x.__str__())
            print('Monthly cost:', monthly, 'kr')
            print('Area cost: ', area, 'kr/kvm')
            print(stripes)
            print_prop.append(x)
    if not properties_exists:
        print('\nNo properties matched your requests!')
    return print_prop


def sorted_properties(properties, settings, interest, deposit, deduction):
    """
    Function to sort properties with chosen parameter from user input
    :param properties: properties to be sorted
    :param settings: Filtrates the properties from user input for settings
    :param interest: User input from beginning of program
    :param deposit: User input from beginning of program
    :param deduction: User input from beginning of program
    :return: Returns all properties with filtration and sorted by a chosen parameter
    """
    sorted_list = []
    user_input = control_lower_letter('Choose one desired parameter to sort properties by: \n')
    if user_input == 'a':
        sorted_list = sorted(properties, key=lambda value: value.monthly_cost(interest, deposit, deduction))
    elif user_input == 'b':
        sorted_list = sorted(properties, key=lambda value: value.rent)
    elif user_input == 'c':
        sorted_list = sorted(properties, key=lambda value: value.area_cost())
    elif user_input == 'd':
        sorted_list = sorted(properties, key=lambda value: value.area)
    return print_properties(sorted_list, settings, interest, deposit, deduction)


def execute(choice, properties, settings, interest, deposit, deduction):
    """
    Function to execute chosen option from menu
    :param choice: User input, assigned a function to execute
    :param properties: list with properties
    :param settings: list with settings
    :param interest: user input
    :param deposit: user input
    :param deduction: user input
    :return:Chosen option
    """
    if choice == 1:
        desired_monthly_cost = control_int('Change desired monthly cost to (kr): ')
        settings[0] = desired_monthly_cost

    elif choice == 2:
        change_rent = control_int('Change desired rent to (kr): ')
        settings[1] = change_rent

    elif choice == 3:
        change_area_cost = control_int('Change desired area cost to (kr): ')
        settings[2] = change_area_cost

    elif choice == 4:
        change_area = control_float('Change desired area to (kvm): ')
        settings[3] = change_area

    elif choice == 5:
        print_properties(properties, settings, interest, deposit, deduction)

    elif choice == 6:
        print(' a - Monthly cost\n', 'b - Rent\n', 'c - Area cost\n', 'd - Area\n')
        matching_properties = sorted_properties(properties, settings, interest, deposit, deduction)
        print_file = control_yes_no('Would you like to print sorted properties to file? Answer Y (yes) or N (no): \n')
        if print_file == 'Y':
            save_properties_to_print_file(matching_properties, 'Print.csv', interest, deposit,
                                          deduction)
            print('\nYour properties were successfully printed to file!\n')
        elif print_file == 'N':
            print('\nYour properties were not printed to file!\n')

    elif choice == 7:
        print('\nPlease enter following property information!')
        property_price = control_int('Price of property: ')
        property_area = control_float('Area of property: ')
        property_rent = control_int('Rent of property: ')
        property_number = input(str('Number to property: '))
        property_address = input(str('Address to property: '))
        new_property = Property(property_price, property_area, property_rent, property_number, property_address)
        properties.append(new_property)
        print('\nYour property was successfully added!\n')

    elif choice == 8:
        print('Here are all of the available properties: ')
        print(stripes)
        for i in properties:
            print(i.__str__())
            print(stripes)
        property_name = control_upper_letter('Please enter property (street address) to remove: ')
        property_exists = False
        for i in properties:
            if property_name == i.address:
                property_exists = True
                properties.remove(i)
                print('\nThe property was successfully removed!\n')
        if not property_exists:
            print('\nThe property does not exist!\n')

    elif choice == 9:
        save_settings_to_file(settings, 'Settings.csv')
        save_properties_to_file(properties, 'Sales.csv')
        print('\nThank you for using Kimberlynet!')


def main():
    """
    Used to "summarize" all code
    :return: List with sorted properties which satisfies the users selection. Saved to a file. Settings saved to file.
    """
    properties = read_properties_from_file('Sales.csv')
    settings = read_settings_from_file('Settings.csv')
    print(stripes)
    print(
        "\nWelcome to Kimberlynet - Sweden's largest residential site\n\nWe will help you find a property, please"
        " answer a few questions before we start!\n")
    print(stripes)
    interest = control_float('Please enter current interest (%): ')
    deposit = control_int('Please enter your deposit: ')
    deduction = control_float('Please enter current deduction (%): ')
    check = False
    while not check:
        menu(settings)
        choice = menu_choice()
        execute(choice, properties, settings, interest, deposit, deduction)
        if choice == 9:
            check = True


main()
