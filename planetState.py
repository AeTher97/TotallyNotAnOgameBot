

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

        'LightFighter',
        'HeavyFighter',
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
        'SolarSatellite',

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

        self._attributes_to_compare = [
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

    def copy(self):

        copy_state = PlanetState()
        for i in self._attributes:
            copy_state.set(i, getattr(self, i))

        return copy_state

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
        for i in self._attributes_to_compare:
                if getattr(self, i) < getattr(other, i):
                    return False
        return True

    def __eq__(self, other):
        for i in self._attributes_to_compare:
            try:
                if getattr(self, i) != getattr(other, i):
                    return False
            except AttributeError:
                return False
        return True

