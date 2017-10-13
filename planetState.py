

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
        "SolarSatellite",
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

