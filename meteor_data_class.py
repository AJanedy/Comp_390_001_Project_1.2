class MeteorDataEntry:
    """ This is the MeteorDataEntry class definition
        Contains variables associated with the attributes of a meteorite """

    def __init__(self, name, id, nametype, rec_class, mass, fall, year, rec_lat, rec_long,
                 geo_location, states, counties):
        super().__init__()
        self.name = name
        self.id = id
        self.nametype = nametype
        self.rec_class = rec_class
        self.mass = mass
        self.fall = fall
        self.year = year
        self.rec_lat = rec_lat
        self.rec_long = rec_long
        self.geo_location = geo_location
        self.states = states
        self.counties = counties
