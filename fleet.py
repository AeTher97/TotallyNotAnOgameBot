

class Fleet:
    def __init__(self):
        self.attributes = [
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

        'Mission',
        'Speed',

        'Metal',
        'Crystal',
        'Deuter'

        ]

        for i in self.attributes:
            if i != 'Speed':
                setattr(self, i, 0)
            else:
                setattr(self,i,100)

        # defenses
        # ships

    def set(self, attr_name, value):
        """
        :param attr_name: string
        :param value: integer
        :raises: ValueError if couldn't find attribute of given name
        :return: True if everything went well
        """
        for i in self.attributes:
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
        for i in self.attributes:
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
        for i in self.attributes:
            if attr_name == i:
                return getattr(self, attr_name)
        raise ValueError("There is no attribute named: " + str(attr_name))

    def __str__(self):
        result = str()
        for i in self.attributes:
            if(i != self.attributes[0]):
                result += "\n"
            result += i + " = " + str(getattr(self, i))
        return result

    def __ge__(self, other):
        """
        :param other: PlanetState object
        :return: if every attribute is greater or equal return True, otherwise return False
        """
        for i in self.attributes:
            if i != "time":
                if getattr(self, i) < getattr(other, i):
                    return False
        return True

