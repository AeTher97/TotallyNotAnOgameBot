

class Fleet:
    def __init__(self):
        self._attributes = [
        'LightFigher',
        'HeavyFigher',
        'Cruiser',
        'Battleship',
        'LightTransport',
        'HeavyTransport',
        'ColonizationShip',
        'Dreadnought',
        'Bomber',
        'Destroyer',
        'DeathStar',
        'Recycler',
        'SpyProbe',

        ]

        for i in self._attributes:
            setattr(self, i, 0)

    def set(self, attr_name, value):
        """
        :param attr_name: string
        :param value: integer
        :raises: ValueError if couldn't find attribute of given name
        :return: True if everything went well
        """
        for i in self._attributes:
            if attr_name == i:
                setattr(self, attr_name, value)
                return True
        raise ValueError("There is no attribute named: " + str(attr_name))

    def set_min(self, attr_name, value):
        """
        sets attribute to value if given value is greater than current one
        :param attr_name: string
        :param value: integer
        :raises: ValueError if couldn't find attribute of given name
        :return: True if everything went well
        """
        for i in self._attributes:
            if attr_name == i:
                if getattr(self, attr_name) < value:
                    setattr(self, attr_name, value)
                return True
        raise ValueError("There is no attribute named: " + str(attr_name))

    def get(self, attr_name):
        """
        :param attr_name: string
        :return: value
        """
        for i in self._attributes:
            if attr_name == i:
                return getattr(self, attr_name)
        raise ValueError("There is no attribute named: " + str(attr_name))
