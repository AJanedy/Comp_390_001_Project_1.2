import os.path
import sys
from io import StringIO
import pytest

from generate_output import *
from user_input import *


def test_get_open_mode_from_user(monkeypatch):

    test_get_open_mode_from_user_with_valid_input(monkeypatch)
    test_get_open_mode_from_user_with_quit_input(monkeypatch)
    test_get_open_mode_from_user_with_invalid_input(monkeypatch)


def test_quit_program():

    with pytest.raises(SystemExit) as result:
        quit_program()
    assert result.type is SystemExit
    assert str(result.value == '\nExiting the program')


def test_create_text_file():

    simulated_meteor_list = []
    simulated_meteor_search = SearchCriteria
    simulated_meteor_search.data_types = []
    file_path = create_text_file(simulated_meteor_search, simulated_meteor_list)
    assert os.path.exists(file_path)


def test_create_excel_file():

    simulated_meteor_list = []
    simulated_meteor_search = SearchCriteria
    simulated_meteor_search.data_types = []
    file_path = create_excel_file(simulated_meteor_search, simulated_meteor_list)
    assert os.path.exists(file_path)


def test_get_open_mode_from_user_with_invalid_input(monkeypatch):

    invalid_input_list = ['z', '45', 'write', '']
    for simulated_input in invalid_input_list:
        with pytest.raises(EOFError) as error:
            captured_output = StringIO()
            sys.stdout = captured_output
            monkeypatch.setattr('sys.stdin', StringIO(simulated_input))
            get_open_mode_from_user()
        assert error.type is EOFError


def test_get_open_mode_from_user_with_quit_input(monkeypatch):

    quit_input_list = ['>q', '>Q']
    for simulated_input in quit_input_list:
        captured_output = StringIO()
        sys.stdout = captured_output
        monkeypatch.setattr('sys.stdin', StringIO(simulated_input))
        with pytest.raises(SystemExit) as result:
            get_open_mode_from_user()
        assert result.type is SystemExit
        assert str(result.value) == '\nExiting the program.'


def test_get_open_mode_from_user_with_valid_input(monkeypatch):

    valid_input_list = ['r', 'w', 'x', 'a']
    for simulated_input in valid_input_list:
        captured_output = StringIO()
        sys.stdout = captured_output
        monkeypatch.setattr('sys.stdin', StringIO(simulated_input))

        assert get_open_mode_from_user() == simulated_input

