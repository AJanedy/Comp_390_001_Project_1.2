"""
text_prompts.py

This module contains functions for printing messages to the terminal

Functions:
    welcome_message() -> None
    list_files_in_directory() -> list_of_files_in_directory: list[str]
    open_mode_prompt() -> None
    attribute_prompt() -> None
    lower_limit_prompt -> None
    upper_limit_prompt -> None
    data_output_prompt() -> None
    invalid_selection() -> None
    quit_program() -> None
    go_again_prompt() -> None
"""

from search_criteria_class import SearchCriteria
from color_class import Colors
from file_operators import search_file_directory


def welcome_message():
    """ displays a centered welcome message to the user """

    line_length = 80
    print()
    print('*' * line_length)
    print(f"{'Welcome to the meteorite filtering program' : ^{line_length}}")
    print(f"{'This program filters a large data set to display a desired range of data' : ^{line_length}}")
    print(f"{'Follow the prompts to filter desired data from a large data file' : ^{line_length}}")
    print(f"{'Program designed and implemented by Andrew Janedy' : ^{line_length}}")
    print(f"{'Release date: October 2023' : ^{line_length}}")
    print('*' * 80)
    print()


def list_files_in_directory():
    """ prints the list of files available in the package directory and also returns that list """

    print("From this list of files:\n")
    list_of_files = search_file_directory()
    print("\nWhich file would you like to open?")
    print("Enter the full name of the file, including the extension,")
    return list_of_files


def open_mode_prompt():
    """ prints the menu for file opening mode """

    print("What mode would you like to open the file with?\n"
          "\"r\" - open for reading (default)\n"
          "\"w\" - open for writing\n"
          "\"x\" - open for exclusive creation, failing if the file already exists\n"
          "\"a\" - open for writing, appending to the end of the file if it exists\n"
          "Enter \">q\" or \">Q\" to quit")


def attribute_prompt():
    """ prints the menu for attribute filtration options """

    print("What attributes would you like to filter the data on?\n"
          "1.  Meteor MASS (g)\n"
          "2.  The YEAR the meteorite fell to earth\n"
          "3.  QUIT\n")


def lower_limit_prompt(meteor_search: SearchCriteria):
    """ prints """

    print(f"\nEnter the lower limit (inclusive) for the meteor's {meteor_search.filter_attribute}")


def upper_limit_prompt(meteor_search: SearchCriteria):
    """ prints """

    print(f"\nEnter the upper limit (inclusive) for the meteor's {meteor_search.filter_attribute}")


def data_output_prompt():
    """ prints the menu for data output option """

    print("\nHow would you like to output the filter results?\n"
          "1. On screen (in terminal)\n"
          "2. To a TEXT file\n"
          "3. To an EXCEL file\n"
          "4. QUIT\n")


def invalid_selection():
    """ prints an error message """

    print(Colors.RED + "\nInvalid selection\n" + Colors.WHITE)


def quit_program():
    """ prints the quit message and quits the program """

    exit("\nExiting the program.")


def go_again_prompt():

    print("\nWould you like to go again?")


