"""
file_operators.py

This module contains functions for manipulating the file data of files contained in the
text_files subdirectory.

Functions:
    search_file_directory() -> os.listdir: list[str]
    create_list_from_file() -> list_of_meteors: list[MeteorDataEntry]
    construct_file_path() -> file_path: str
    build_list() -> list_of_meteors: list[MeteorDataEntry]
    fill_blank_data() -> list[str]
    split_line_by_tab() -> list[str]
    get_how_many_attributes() -> count: int
"""

import os
from color_class import Colors
from meteor_data_class import MeteorDataEntry


def search_file_directory():
    """ opens the file directory and prints each filename to the terminal """

    file_directory = "text_files"
    for file in os.listdir(file_directory):
        print(file)
    return os.listdir(file_directory)


def create_list_from_file(meteor_search):
    """ returns a list of MeteorDataEntry objects built from the chosen file """

    file_path = construct_file_path(meteor_search)
    try:
        with open(file_path, meteor_search.open_mode) as file:
            list_of_meteors = build_list(file, meteor_search)

            return list_of_meteors

    except FileNotFoundError:
        print(Colors.RED + "File not found" + Colors.WHITE)


def construct_file_path(meteor_search):
    """ constructs the absolute file path based on the current directory "__file__",
        the subdirectory text_files, and the filename chosen by the user """

    current_directory = os.path.dirname(os.path.abspath(__file__))
    relative_path = os.path.join('text_files', meteor_search.filename)
    file_path = os.path.join(current_directory, relative_path)
    return file_path


def build_list(file, meteor_search):
    """ creates a MeteorDataEntry object from each line in the file and returns
        a list of those objects """

    list_of_meteors = []
    count = get_how_many_attributes(file, meteor_search)

    for line in file:
        line_as_list = split_line_by_tab(line)

        if len(line_as_list) == count:
            list_of_meteors.append(MeteorDataEntry(*line_as_list))

        # replaces missing elements in list with incomplete data
        if len(line_as_list) < count:
            line_as_list = fill_blank_data(count, line_as_list)
            list_of_meteors.append(MeteorDataEntry(*line_as_list))
    return list_of_meteors


def fill_blank_data(count, line_as_list):
    """ if a data set in the list is incomplete, this function appends the list with
        empty strings until it matches the required length """

    for i in range(count - len(line_as_list)):
        line_as_list.append('')
    return line_as_list


def split_line_by_tab(line):
    """ creates a list of tab separated strings """

    line_as_string = line.strip('\n')
    line_as_list = line_as_string.split('\t')
    return line_as_list


def get_how_many_attributes(file, meteor_search):
    """ determines how many pieces of data are in each line of the given file
        while also saving the data types to be used when we display our data """

    data_type_headers = file.readline().split('\t')
    meteor_search.data_types = data_type_headers
    count = sum(1 for string in data_type_headers if string.strip())
    return count
