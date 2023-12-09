class SearchCriteria:
    """ This is the SearchCriteria class definition
        Contains variables associated with the attributes of the user's specific search """
    def __init__(self):
        self.filename: str = ''
        self.open_mode: chr = ''
        self.filter_attribute: str = ''
        self.lower_limit: int = 0
        self.upper_limit: int = 0
        self.output_option: str = ''
        self.all_meteors = []
        self.data_types = []




