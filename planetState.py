

class PlanetState:
    def __init__(self):
        self._attributes = ["metal",
        "crystal",
        "deuter",
        "energy",
        "temperature",

        "PlanetSize",

        "Galaxy",
        "Star",
        "Planet",

        "MetalMine",
        "CrystalMine",
        "DeuterExtractor",
        "SolarPowerPlant",
        "FusionPowerPlant",
        "MetalStorage",
        "CrystalStorage",
        "DeuterStorage",

        "RobotFactory",
        "Shipyard",
        "Laboratory",
        "AllayDepot",
        "RocketSilo",
        "NaniteFactory",
        "Terraformer",
        "SpaceDock",

        "EnergyTechnology",
        "LaserTechnology",
        "IonTechnology",
        "HyperspaceTechnology",
        "PlasmaTechnology",
        "CombustionDrive",
        "ImpulseDrive",
        "HyperDrive",
        "SpyTechnology",
        "ComputerTechnology",
        "Astrophysics",
        "IntergalacticResearchNetwork",
        "GravitonDevelopment",
        "BattleTechnology",
        "ShieldingTechnology",
        "Armor",

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
        'SpySatellite',
        'SolarSatellite'

        'RocketLauncher',
        'LightLaserCannon',
        'HeavyLaserCannon',
        'GaussCannon',
        'IonCannon',
        'PlasmaLauncher',
        'SmallPlanetaryShield',
        'LargePlanetaryShield',
        'AntiMissile',
        'InterplanetaryMissile'
        ]

        for i in self._attributes:
            setattr(self, i, 0)

        # defenses
        # ships

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

    def add(self, attr_name, value):
        """
        :param attr_name: string
        :param value: integer
        :raises: ValueError if couldn't find attribute of given name
        :return: True if everything went well
        """
        for i in self._attributes:
            if attr_name == i:
                setattr(self, attr_name, value + getattr(self, attr_name))
                return True
        raise ValueError("There is no attribute named: " + str(attr_name))

    def __str__(self):
        result = str()
        for i in self._attributes:
            if(i != self._attributes[0]):
                result += "\n"
            result += i + " = " + str(getattr(self, i))
        return result

    def __ge__(self, other):
        """
        :param other: PlanetState object
        :return: if every attribute is greater or equal return True, otherwise return False
        """
        for i in self._attributes:
            if i != "time":
                if getattr(self, i) < getattr(other, i):
                    return False
        return True

