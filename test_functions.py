"""
test_functions.py contains unit tests for various functions in the
Comp_390_001_Project_1.2 package.

Tested functions:
    quit_program()
    get_open_mode_from_user()
    get_lower_limit_from_user()
    get_text_file_path()
    get_excel_file_path()
    create_text_file()
    create_excel_file()
"""

import sys
from io import StringIO
import pytest
from generate_output import *
from user_input import *


def test_quit_program():
    """ tests the quit_program() function, which exits the program via
        exit() and prints 'Exiting the program' to the terminal """

    with pytest.raises(SystemExit) as result:
        quit_program()
    assert result.type is SystemExit
    assert str(result.value == '\nExiting the program')


def test_get_open_mode_from_user_with_valid_input(monkeypatch):
    """ tests the get_open_mode_from_user() function with valid input.
        valid_input_list represents the only input this function will accept
        (without exiting the program).  upon entering the valid input the
        function returns the input as a string. """

    valid_input_list = ['r', 'w', 'x', 'a']
    for simulated_input in valid_input_list:
        captured_output = StringIO()
        sys.stdout = captured_output
        monkeypatch.setattr('sys.stdin', StringIO(simulated_input))

        assert get_open_mode_from_user() == simulated_input


def test_get_open_mode_from_user_with_invalid_input(monkeypatch):
    """ tests the get_open_mode_from_user() function with invalid input.
        invalid_input_list represents simulated user input that will be rejected.
        upon entering the invalid input the function calls itself to prompt for
        valid input.  In this context it raises an EOFError """

    invalid_input_list = ['z', '45', 'write', '', '\n']
    for simulated_input in invalid_input_list:
        with pytest.raises(EOFError) as error:
            captured_output = StringIO()
            sys.stdout = captured_output
            monkeypatch.setattr('sys.stdin', StringIO(simulated_input))
            get_open_mode_from_user()
        assert error.type is EOFError


def test_get_open_mode_from_user_with_quit_input(monkeypatch):
    """ tests the get_open_mode_from_user() function with 'quit' input.
        quit_input_list represents input that will call the quit_program() function. """

    quit_input_list = ['>q', '>Q']
    for simulated_input in quit_input_list:
        captured_output = StringIO()
        sys.stdout = captured_output
        monkeypatch.setattr('sys.stdin', StringIO(simulated_input))
        with pytest.raises(SystemExit) as result:
            get_open_mode_from_user()
        assert result.type is SystemExit
        assert str(result.value) == '\nExiting the program.'


def test_get_lower_limit_from_user_with_valid_input(monkeypatch):
    """ tests the get_lower_limit_from_user() function with valid input.
        valid_input_list represents the only input this function will accept
        (without exiting the program).  upon entering the valid input the
        function returns the input as a string. """

    valid_input_list = ['0', '5', '100', '290,0000']
    simulated_meteor_search = SearchCriteria
    simulated_meteor_search.filter_attribute = "filler text"
    for simulated_input in valid_input_list:
        captured_output = StringIO()
        sys.stdout = captured_output
        monkeypatch.setattr('sys.stdin', StringIO(simulated_input))

        assert get_lower_limit_from_user(simulated_meteor_search) == \
               simulated_input.replace(',', '')


def test_get_lower_limit_from_user_with_invalid_input(monkeypatch):
    """ tests the get_lower_limit_from_user() function with invalid input.
        invalid_input_list represents simulated user input that will be rejected
        upon entering the invalid input the program will call itself until it gets
        valid input.  in this context it raises an EOFError """

    invalid_input_list = [',m', '\n', 'cory', 'one hundred']
    simulated_meteor_search = SearchCriteria
    simulated_meteor_search.filter_attribute = "filler text"
    for simulated_input in invalid_input_list:
        with pytest.raises(EOFError) as error:
            captured_output = StringIO()
            sys.stdout = captured_output
            monkeypatch.setattr('sys.stdin', StringIO(simulated_input))
            get_lower_limit_from_user(simulated_meteor_search)
        assert error.type == EOFError


def test_get_lower_limit_from_user_with_quit_input(monkeypatch):
    """ tests the get_lower_limit_from_user() function with 'quit' input.
        quit_input_list represents input that will call the quit_program() function. """

    quit_input_list = ['Q']
    simulated_meteor_search = SearchCriteria
    simulated_meteor_search.filter_attribute = "filler text"
    for simulated_input in quit_input_list:
        captured_output = StringIO()
        sys.stdout = captured_output
        monkeypatch.setattr('sys.stdin', StringIO(simulated_input))
        with pytest.raises(SystemExit) as result:
            get_lower_limit_from_user(simulated_meteor_search)
        assert result.type is SystemExit
        assert str(result.value) == '\nExiting the program.'


def test_get_text_file_path():
    """ calls the get_text_file_path() function and checks to see if it contains
        certain invalid filename characters, ensures that there is only 1 period in the
        filename, and ensures that the filename ends with '.txt' """

    invalid_characters_list = ['<', '>', ':', ';', '\"', '\'', '|', '?', '*']
    count = 0

    for character in invalid_characters_list:
        assert character not in get_text_file_path()
    for character in get_text_file_path():
        if character == '.':
            count += 1
    assert count == 1
    assert get_text_file_path().endswith('.txt')


def test_get_excel_file_path():
    """ calls the get_excel_file_path() function and checks to see if it contains
        certain invalid filename characters, ensures that there is only 1 period in the
        filename, and ensures that the filename ends with '.txt' """

    invalid_characters_list = ['<', '>', ':', ';', '\"', '\'', '|', '?', '*']
    count = 0

    for character in invalid_characters_list:
        assert character not in get_text_file_path()
    for character in get_excel_file_path():
        if character == '.':
            count += 1
    assert count == 1
    assert get_excel_file_path().endswith('.xls')


def test_create_text_file():
    """ creates an empty list and a SearchCritera object (with the attribute needed
        to pass into create_text_file), and checks to see if create_text_file
        creates a .txt file within the directory """

    simulated_meteor_list = []
    simulated_meteor_search = SearchCriteria
    simulated_meteor_search.data_types = []
    file_path = create_text_file(simulated_meteor_search, simulated_meteor_list)
    assert os.path.exists(file_path)


def test_create_excel_file():
    """ creates an empty list and a SearchCritera object (with the attribute needed
        to pass into create_excel_file), and checks to see if create_excel_file
        creates a .xls file within the directory """

    simulated_meteor_list = []
    simulated_meteor_search = SearchCriteria
    simulated_meteor_search.data_types = []
    file_path = create_excel_file(simulated_meteor_search, simulated_meteor_list)
    assert os.path.exists(file_path)
