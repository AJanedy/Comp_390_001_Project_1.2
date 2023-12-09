"""
generate_output.py

This module contains functions for handling and printing data to either the terminal,
a .txt file, or a .xls file.

Functions:
    generate_user_specified_output() -> None
    print_header() -> None
    print_data_to_terminal() -> None
    create_text_file() -> None
    create_excel_file() -> None
    print_first_line_in_text_file() -> None
    print_data_to_text_file() -> None
    get_text_file_path() -> file_path: str
    get_datetime_string() -> clean_timestamp_string: str
    populate_excel_sheet_data() -> None
    populate_excel_sheet_header_row() -> None
    get_excel_file_path() -> file_path: str
"""

import os
from xlwt import Workbook
from datetime import datetime


def generate_user_specified_output(meteor_search, meteor_list):
    """ reads the output_option attribute from the class attributes of :param meteor_search
        and sends the :param meteor_list to the associated function for processing """

    if meteor_search.output_option == 'TERMINAL':
        print_header(meteor_search)
        print_data_to_terminal(meteor_list)
    elif meteor_search.output_option == 'TEXT':
        create_text_file(meteor_search, meteor_list)
    elif meteor_search.output_option == 'EXCEL':
        create_excel_file(meteor_search, meteor_list)
    else:
        print("Not enough information.  Please try again")
        return None


def print_header(meteor_search):
    """ prints the first line to the terminal; a line containing the data_type(s)
        for each corresponding column of data.  """

    print('\n      ', end='')  # indent formatting
    max_width = 24

    for data_type in meteor_search.data_types:
        print(f'{data_type.strip():<{max_width}}', end='')
    print()
    print("=" * (len(meteor_search.data_types) * max_width))


def print_data_to_terminal(meteor_list):
    """ iterates through the list of MeteorDataEntry class objects, unpacks each class
        object into a corresponding dictionary, then iterates through each
        dictionary to print each dictionary value to the terminal """

    count = 1
    max_width = 24

    #  for each MeteorDataEntry object in the list
    for meteor in meteor_list:
        print(f'{count:<6}', end='')  # indent
        meteor_dict = vars(meteor)  # vars() unpacks each MeteorDataEntry object and makes a dictionary

        #  for each value in each MeteorDataEntry dictionary
        for _, data in meteor_dict.items():
            print(f'{data:<{max_width}}', end='')
        print()
        count += 1


def create_text_file(meteor_search, meteor_list):
    """ opens a new file for writing and calls related functions to populate
        that file.  """

    file_path = get_text_file_path()

    with open(file_path, 'w') as file:
        print_first_line_in_text_file(file, meteor_search)
        print_data_to_text_file(file, meteor_list)

    return file_path


def get_text_file_path():
    """ builds the filepath for the program to create a new .txt file """

    datetime_as_filename = get_datetime_string()
    datetime_as_filename = datetime_as_filename + '.txt'
    subdirectory = "text_files"
    file_path = os.path.join(subdirectory, datetime_as_filename)
    return file_path


def print_first_line_in_text_file(file, meteor_search):
    """ prints the first line to the file; a string containing each data type separated
        by tab characters """

    for item in meteor_search.data_types:
        file.write(f'{item.strip()}\t')
    file.write('\n')


def print_data_to_text_file(file, meteor_list):
    """ prints to the file a line for each meteor in the meteor_list.  each meteor attribute
        is separated by a tab character and a newline is placed after the final attribute """
    for meteor in meteor_list:
        all_data = vars(meteor)
        for _, data in all_data.items():
            file.write(f'{data.strip()}\t')
        file.write('\n')


def get_datetime_string():
    """ gets the current time from the system's internal clock and from it
        formats a string that satisfies Window's file naming standards, then
        :returns clean_time_stamp_string """

    current_timestamp = datetime.now()
    current_timestamp.strftime("%Y-%m-%d %H-%M-%S")
    clean_timestamp_string = current_timestamp.__str__().replace(':', '_')
    clean_timestamp_string = clean_timestamp_string.replace('.', '_')
    clean_timestamp_string = clean_timestamp_string.replace(' ', '_')
    return clean_timestamp_string


def create_excel_file(meteor_search, meteor_list):
    """ creates a new Excel workbook object and creates an Excel file
        containing each meteorite from the search criteria, then saves it to
         the subdirectory "excel_files" """

    data_sheet, file_path, workbook = initialize_new_excel_file()

    populate_excel_sheet_header_row(data_sheet, meteor_search)
    populate_excel_sheet_data(data_sheet, meteor_list)

    workbook.save(file_path)

    return file_path


def populate_excel_sheet_data(data_sheet, meteor_list):
    """ populates a new Excel file with the data previous gathered for the user """

    row = 1
    column = 0
    for meteorite in meteor_list:

        all_data = vars(meteorite)
        for _, data in all_data.items():
            data_sheet.write(row, column, data)
            column += 1
        column = 0
        row += 1


def populate_excel_sheet_header_row(data_sheet, meteor_search):
    """ writes the header row to the new Excel file using the data types gathered
        from the header row of the incoming text file """

    column = 0
    for data_type in meteor_search.data_types:
        data_sheet.write(0, column, data_type)
        column += 1


def initialize_new_excel_file():
    """ creates a new Excel file and returns all relevant values associated
        with that file """

    file_path = get_excel_file_path()
    workbook = Workbook()
    data_sheet = workbook.add_sheet("Meteorites")
    return data_sheet, file_path, workbook


def get_excel_file_path():
    """ builds the filepath for the program to create a new .xls file """

    datetime_as_filename = get_datetime_string()
    datetime_as_filename = datetime_as_filename + '.xls'
    subdirectory = "excel_files"
    file_path = os.path.join(subdirectory, datetime_as_filename)
    return file_path
