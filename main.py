"""
main module: this script is designed to open a .txt file of the user's choosing, parse
the data within that file, and filter out specific data as specified by the user.  It
then takes that filtered data and outputs it as either a .txt file, a .xls file, or prints
it to the terminal (user's choice).  .txt files and .xls files will be put in the text_files
or excel_files subdirectory, respectively.
"""

from data_crunchers import filter_meteor_data
from file_operators import create_list_from_file
from generate_output import generate_user_specified_output
from user_input import *
from search_criteria_class import SearchCriteria
from text_prompts import welcome_message

meteor_search_criteria = SearchCriteria()


def main():
    """ main function of the program.  takes no arguments and loops continuously until
        the user quits.  begins with a printed message to the terminal then calls the
        functions related to the functionality of the program """
    welcome_message()
    while True:
        initiate_meteor_search()
        user_searched_meteor_list = filter_meteor_data(meteor_search_criteria)
        generate_user_specified_output(meteor_search_criteria, user_searched_meteor_list)
        go_again()


def initiate_meteor_search():
    """ assigns all attributes of meteor_search_criteria by calling each attribute's
        associated function from the user_input module """

    meteor_search_criteria.filename = get_target_file_from_user()
    meteor_search_criteria.open_mode = get_open_mode_from_user()
    meteor_search_criteria.all_meteors = create_list_from_file(meteor_search_criteria)
    meteor_search_criteria.filter_attribute = get_attribute_from_user()
    meteor_search_criteria.lower_limit = get_lower_limit_from_user(meteor_search_criteria)
    meteor_search_criteria.upper_limit = get_upper_limit_from_user(meteor_search_criteria)
    meteor_search_criteria.output_option = get_output_option_from_user()


main()
