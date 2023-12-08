import sys
from io import StringIO
import pytest
from user_input import *


def test_get_open_mode_from_user(monkeypatch, capfd):

    valid_input_list = ['r', 'w', 'x', 'a']

    for simulated_input in valid_input_list:

        captured_output = StringIO()
        sys.stdout = captured_output
        monkeypatch.setattr('sys.stdin', StringIO(simulated_input))
        # out, err = capfd.readouterr()

        assert get_open_mode_from_user() == simulated_input

def test_quit_program():

    # captured_output = StringIO()
    # sys.stdout = captured_output

    with pytest.raises(SystemExit) as excinfo:
        exit_message = str(excinfo.value)
        exit_code = excinfo.value.code

        assert exit_message == "\nExiting the program."













    # quit_input_list = ['>q', '>Q']

    # with pytest.raises(SystemExit) as outcome:
    #     for simulated_input in quit_input_list:
    #         captured_output = StringIO
    #         sys.stdout = captured_output
    #         monkeypatch.setattr('sys.stdin', StringIO(simulated_input))
    #         with pytest.raises(SystemExit):
    #             get_open_mode_from_user()
    #         assert outcome.type is SystemExit
    #
    #
    # # invalid_input_list = ['t', 'z', [1, 2, 3], "Sam"]

