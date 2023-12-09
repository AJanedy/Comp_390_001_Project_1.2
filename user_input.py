"""
user_input.py

This module contains functions for handling user_input.  each function returns a
value that will be stored in the session's associated SearchCriteria class instance,

Functions:
    get_target_file_from_user() -> target_file: str
    get_open_mode_from_user() -> open_mode: str
    get_attribute_from_user() -> chosen_attribute: str
    convert_chosen_attribute_to_string() -> chosen_attribute: str
    get_lower_limit_from_user() -> lower_limit: str
    get_upper_limit_from_user() -> upper_limit: str
    get_output_option_from_user() -> output_option: str
    convert_output_option_to_string() -> output_option: str
    go_again() -> None
"""


from text_prompts import *
from utility_functions import _string_is_numerical
from search_criteria_class import SearchCriteria
from color_class import Colors


def get_target_file_from_user():
    """ gets target file from user and returns the filename as a string """

    list_of_files = list_files_in_directory()
    target_file = input("Or enter \">q\" or \">Q\" to quit: ")

    if target_file == '>q' or target_file == '>Q':
        quit_program()

    elif target_file in list_of_files:
        print(Colors.GREEN + f"\nTarget file: {target_file}\n" + Colors.WHITE)
        return target_file
    else:
        invalid_selection()
        return get_target_file_from_user()


def get_open_mode_from_user():
    """ returns the user's selection for the file open mode """

    open_mode_prompt()

    mode_options = ['r', 'w', 'x', 'a']
    open_mode = input("Mode --> ")

    if open_mode == '>q' or open_mode == '>Q':
        quit_program()

    elif open_mode in mode_options:
        print(Colors.GREEN + f"\nFile mode: {open_mode}\n" + Colors.WHITE)
        return open_mode

    else:
        invalid_selection()
        return get_open_mode_from_user()


def get_attribute_from_user():
    """ returns the user's selection for the attribute the program will search the file for """

    attribute_prompt()
    chosen_attribute = input("Enter the number of your choice: ")

    # input error check
    if not chosen_attribute.isdigit() or int(chosen_attribute) not in (1, 2, 3):
        invalid_selection()
        return get_attribute_from_user()

    chosen_attribute = convert_chosen_attribute_to_string(chosen_attribute)

    return chosen_attribute


def convert_chosen_attribute_to_string(chosen_attribute):
    """ returns the string of the users chosen attribute converted from its representative int """

    if int(chosen_attribute) == 3:
        quit_program()
    elif int(chosen_attribute) == 2:
        chosen_attribute = "YEAR"
    elif int(chosen_attribute) == 1:
        chosen_attribute = "MASS (g)"
    return chosen_attribute


def get_lower_limit_from_user(meteor_search):
    """ gets the user's selection for the lower limit of the search criteria
        and returns it """

    lower_limit_prompt(meteor_search)
    lower_limit = input("Enter \"Q\" to quit: ").replace(',', '')

    if lower_limit == 'Q':
        quit_program()
    elif not _string_is_numerical(lower_limit):
        invalid_selection()
        return get_lower_limit_from_user(meteor_search)
    return lower_limit


def get_upper_limit_from_user(meteor_search):
    """ gets the user's selection for the upper limit of the search criteria
        and returns it """

    upper_limit_prompt(meteor_search)
    upper_limit = input("Enter \"Q\" to quit: ").replace(',', '')

    if upper_limit == 'Q':
        quit_program()
    elif not _string_is_numerical(upper_limit):
        invalid_selection()
        return get_upper_limit_from_user(meteor_search)
    return upper_limit


def get_output_option_from_user():
    """ gets the user's selection for the output option of their chosen data
        and returns it """

    data_output_prompt()
    output_option = input("Enter the number of your choice: ")

    # input error check
    if not output_option.isdigit() or int(output_option) not in (1, 2, 3, 4):
        invalid_selection()
        return get_output_option_from_user()

    output_option = convert_output_option_to_string(output_option)

    return output_option


def convert_output_option_to_string(output_option):
    """ returns the string of the users chosen output option converted from its representative int """

    if int(output_option) == 4:
        quit_program()
    elif int(output_option) == 3:
        output_option = "EXCEL"
    elif int(output_option) == 2:
        output_option = "TEXT"
    elif int(output_option) == 1:
        output_option = "TERMINAL"
    return output_option


def go_again():
    """ asks the user if they would like to run the program again, option
        to quit otherwise """

    go_again_prompt()
    go_again_choice = input("Press \"n\" or \"N\" to quit program, anything else to continue: ")
    print()
    if go_again_choice == 'n' or go_again_choice == 'N':
        quit_program()
