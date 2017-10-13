from planetState import PlanetState

import math


def getRequirementsTech(planet_state):
    result = Requirements()
    for i in result._attributes:

        # Resource Buildings

        if i == "MetalMine":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)

        if i == "CrystalMine":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)

        if i == "DeuterExtractor":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)

        if i == "SolarPowerPlant":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)

        if i == "FusionPowerPlant":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("EnergyTechnology", 3)
                result.set_min("DeuterExtractor", 5)

        if i == "MetalStorage":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)

        if i == "CrystalStorage":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)

        if i == "DeuterStorage":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)

        # Station Buildings

        if i == "RobotFactory":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)

        if i == "Shipyard":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("RobotFactory", 2)

        if i == "Laboratory":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)

        if i == "AllayDepot":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)

        if i == "RocketSilo":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Shipyard", 1)
                result.set_min("RobotFactory", 2)

        if i == "NaniteFactory":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("RobotFactory", 10)
                result.set_min("ComputerTechnology", 10)
                result.set_min("Laboratory", 1)

        if i == "Terraformer":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("RobotFactory", 10)
                result.set_min("ComputerTechnology", 10)
                result.set_min("EnergyTechnology", 12)
                result.set_min("Laboratory", 1)

        if i == "SpaceDock":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("RobotFactory", 2)

        # Research

        if i == "EnergyTechnology":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Laboratory", 1)

        if i == "LaserTechnology":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Laboratory", 1)
                result.set_min("EnergyTechnology", 2)

        if i == "IonTechnology":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Laboratory", 4)
                result.set_min("EnergyTechnology", 4)
                result.set_min("LaserTechnology", 5)

        if i == "HyperspaceTechnology":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Laboratory", 7)
                result.set_min("EnergyTechnology", 5)
                result.set_min("ShieldingTechnology", 5)

        if i == "PlasmaTechnology":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Laboratory", 4)
                result.set_min("EnergyTechnology", 8)
                result.set_min("LaserTechnology", 10)
                result.set_min("IonTechnology", 5)

        if i == "CombustionDrive":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Laboratory", 1)
                result.set_min("EnergyTechnology", 1)

        if i == "ImpulseDrive":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Laboratory", 2)
                result.set_min("EnergyTechnology", 1)

        if i == "HyperDrive":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Laboratory", 7)
                result.set_min("EnergyTechnology", 5)
                result.set_min("ShieldingTechnology", 5)
                result.set_min("HyperspaceTechnology", 3)

        if i == "SpyTechnology":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Laboratory", 3)

        if i == "ComputerTechnology":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Laboratory", 1)

        if i == "Astrophysics":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Laboratory", 3)
                result.set_min("SpyTechnology", 4)
                result.set_min("ImpulseDrive", 3)
                result.set_min("EnergyTechnology", 1)

        if i == "IntergalacticResearchNetwork":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Laboratory", 10)
                result.set_min("ComputerTechnology", 8)
                result.set_min("HyperspaceTechnology", 8)
                result.set_min("EnergyTechnology", 5)
                result.set_min("ShieldingTechnology", 5)

        if i == "GravitonDevelopment":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Laboratory", 12)

        if i == "BattleTechnology":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Laboratory", 4)

        if i == "ShieldingTechnology":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Laboratory", 6)
                result.set_min("EnergyTechnology", 3)

        if i == "Armor":
            if planet_state.get(i) == 0:
                result.set_min(i, 0)
            else:
                result.set_min(i, planet_state.get(i) - 1)
                result.set_min("Laboratory", 2)

        # Ships

        if i == "LightFighter":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 1)
                result.set_min("RobotFactory", 2)
                result.set_min("CombustionDrive", 1)
                result.set_min("Laboratory", 1)
                result.set_min("EnergyTechnology", 1)

        if i == "HeavyFigher":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 3)
                result.set_min("RobotFactory", 2)
                result.set_min("ImpulseDrive", 2)
                result.set_min("Laboratory", 2)
                result.set_min("EnergyTechnology", 1)
                result.set_min("Armor", 2)

        if i == "Cruiser":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 5)
                result.set_min("RobotFactory", 2)
                result.set_min("ImpulseDrive", 4)
                result.set_min("IonTechnology", 2)
                result.set_min("Laboratory", 4)
                result.set_min("EnergyTechnology", 4)
                result.set_min("LaserTechnology", 5)

        if i == "Battleship":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 7)
                result.set_min("RobotFactory", 2)
                result.set_min("HyperDrive", 4)
                result.set_min("Laboratory", 7)
                result.set_min("EnergyTechnology", 5)
                result.set_min("ShieldingTechnology", 5)
                result.set_min("HyperspaceTechnology", 3)

        if i == "LightTransport":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 2)
                result.set_min("RobotFactory", 2)
                result.set_min("CombustionDrive", 2)
                result.set_min("Laboratory", 1)
                result.set_min("EnergyTechnology", 1)

        if i == "HeavyTransport":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 4)
                result.set_min("RobotFactory", 2)
                result.set_min("CombustionDrive", 6)
                result.set_min("Laboratory", 1)
                result.set_min("EnergyTechnology", 1)

        if i == "ColonizationShip":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 4)
                result.set_min("RobotFactory", 2)
                result.set_min("ImpulseDrive", 3)
                result.set_min("Laboratory", 2)
                result.set_min("EnergyTechnology", 1)

        if i == "Dreadnought":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 8)
                result.set_min("RobotFactory", 2)
                result.set_min("HyperDrive", 5)
                result.set_min("Laboratory", 7)
                result.set_min("EnergyTechnology", 5)
                result.set_min("ShieldingTechnology", 5)
                result.set_min("HyperspaceTechnology", 5)
                result.set_min("LaserTechnology", 12)

        if i == "Bomber":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 8)
                result.set_min("RobotFactory", 2)
                result.set_min("ImpulseDrive", 6)
                result.set_min("PlasmaTechnology", 5)
                result.set_min("Laboratory", 4)
                result.set_min("EnergyTechnology", 8)
                result.set_min("LaserTechnology", 10)
                result.set_min("IonTechnology", 5)

        if i == "Destroyer":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 9)
                result.set_min("RobotFactory", 2)
                result.set_min("HyperDrive", 6)
                result.set_min("Laboratory", 7)
                result.set_min("EnergyTechnology", 5)
                result.set_min("ShieldingTechnology", 5)
                result.set_min("HyperspaceTechnology", 5)

        if i == "DeathStar":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 12)
                result.set_min("RobotFactory", 2)
                result.set_min("HyperDrive", 7)
                result.set_min("Laboratory", 12)
                result.set_min("EnergyTechnology", 5)
                result.set_min("ShieldingTechnology", 5)
                result.set_min("HyperspaceTechnology", 6)
                result.set_min("GravitonDevelopment", 1)

        if i == "Recycler":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 4)
                result.set_min("RobotFactory", 2)
                result.set_min("CombustionDrive", 6)
                result.set_min("ShieldingTechnology", 2)
                result.set_min("Laboratory", 6)
                result.set_min("EnergyTechnology", 3)

        if i == "Recycler":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 4)
                result.set_min("RobotFactory", 2)
                result.set_min("CombustionDrive", 6)
                result.set_min("ShieldingTechnology", 2)
                result.set_min("Laboratory", 6)
                result.set_min("EnergyTechnology", 3)

        if i == "SpyProbe":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 3)
                result.set_min("RobotFactory", 2)
                result.set_min("CombustionDrive", 3)
                result.set_min("EnergyTechnology", 1)
                result.set_min("SpyTechnology", 2)
                result.set_min("Laboratory", 3)

        if i == "SolarSatellite":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 1)
                result.set_min("RobotFactory", 2)


    return result


class Requirements(PlanetState):
    def __init__(self):
        super(Requirements, self).__init__()
        self._attributes.append("time")
        setattr(self, self._attributes[-1], 0)
