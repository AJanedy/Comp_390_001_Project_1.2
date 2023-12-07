from search_criteria import SearchCriteria


def filter_meteor_data(meteor_search):
    """ calls the list building function associated with the given filter attribute criteria
        and returns the list assembled by that function """

    if meteor_search.filter_attribute == "MASS (g)":
        return build_mass_list(meteor_search)
    if meteor_search.filter_attribute == "YEAR":
        return build_year_list(meteor_search)


def build_mass_list(meteor_search):
    """ builds and returns a list of meteors based on the user's chosen upper and lower limits
        for the meteor's mass """

    list_of_meteors_by_mass = []
    for meteor in meteor_search.all_meteors:
        if meteor.mass.isdigit() and \
                float(meteor_search.lower_limit) <= float(meteor.mass) <= float(meteor_search.upper_limit):
            list_of_meteors_by_mass.append(meteor)
    return list_of_meteors_by_mass


def build_year_list(meteor_search):
    """ builds and returns a list of meteors based on the user's chosen upper and lower limits
        for the meteor's year """

    list_of_meteors_by_year = []
    for meteor in meteor_search.all_meteors:
        if meteor.year.isdigit() and \
                float(meteor_search.lower_limit) <= float(meteor.year) <= float(meteor_search.upper_limit):
            list_of_meteors_by_year.append(meteor)
    return list_of_meteors_by_year
