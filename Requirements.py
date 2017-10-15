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

        if i == "HeavyFighter":
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

        # Defenses

        if i == "RocketLauncher":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 1)
                result.set_min("RobotFactory", 2)

        if i == "LightLaserCannon":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 2)
                result.set_min("RobotFactory", 2)
                result.set_min("EnergyTechnology", 2)
                result.set_min("LaserTechnology", 3)
                result.set_min("Laboratory", 1)

        if i == "HeavyLaserCannon":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 4)
                result.set_min("RobotFactory", 2)
                result.set_min("EnergyTechnology", 3)
                result.set_min("LaserTechnology", 6)
                result.set_min("Laboratory", 1)

        if i == "GaussCannon":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 6)
                result.set_min("RobotFactory", 2)
                result.set_min("EnergyTechnology", 6)
                result.set_min("BattleTechnology", 4)
                result.set_min("ShieldingTechnology", 1)
                result.set_min("Laboratory", 6)

        if i == "IonCannon":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 4)
                result.set_min("RobotFactory", 2)
                result.set_min("IonTechnology", 6)
                result.set_min("Laboratory", 4)
                result.set_min("EnergyTechnology", 4)
                result.set_min("LaserTechnology", 5)

        if i == "PlasmaLauncher":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 8)
                result.set_min("RobotFactory", 2)
                result.set_min("PlasmaTechnology", 6)
                result.set_min("Laboratory", 4)
                result.set_min("EnergyTechnology", 8)
                result.set_min("LaserTechnology", 10)
                result.set_min("IonTechnology", 5)

        if i == "SmallPlanetaryShield":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 1)
                result.set_min("RobotFactory", 2)
                result.set_min("ShieldingTechnology", 2)
                result.set_min("Laboratory", 6)
                result.set_min("EnergyTechnology", 3)

        if i == "LargePlanetaryShield":
            if planet_state.get(i) > 0:
                result.set_min("Shipyard", 6)
                result.set_min("RobotFactory", 2)
                result.set_min("ShieldingTechnology", 6)
                result.set_min("Laboratory", 6)
                result.set_min("EnergyTechnology", 3)

        if i == "AntiMissile":
            if planet_state.get(i) > 0:
                result.set_min("RocketSilo", 2)
                result.set_min("Shipyard", 1)
                result.set_min("RobotFactory", 2)

        if i == "InterplanetaryMissile":
            if planet_state.get(i) > 0:
                result.set_min("RocketSilo", 4)
                result.set_min("Shipyard", 1)
                result.set_min("RobotFactory", 2)
                result.set_min("ImpulseDrive", 1)
                result.set_min("Laboratory", 2)
                result.set_min("EnergyTechnology", 1)

    return result

def getRequirementsRes(current_state, wanted_state):
    """
    Returns how much resources you need to go from current state to wanted state.
    Warning! It doesn't check if such transition is possible
    :param current_state:
    :param wanted_state:
    :return: Current state with needed resources
    """
    result = Requirements()
    for i in result._attributes:
        if i == "metal":
            result.set(i, wanted_state.get(i))
        if i == "crystal":
            result.set(i, wanted_state.get(i))
        if i == "deuter":
            result.set(i, wanted_state.get(i))
        if i == "energy":
            result.set(i, wanted_state.get(i))

        if i == "MetalMine":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(60 * math.pow(1.5, lvl - 1)))
                    result.add("crystal", math.floor(15 * math.pow(1.5, lvl - 1)))
                    result.add("energy", math.ceil(10 * lvl * math.pow(1.1, lvl)))

        if i == "CrystalMine":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(48 * math.pow(1.5, lvl - 1)))
                    result.add("crystal", math.floor(24 * math.pow(1.5, lvl - 1)))
                    result.add("energy", math.ceil(10 * lvl * math.pow(1.1, lvl)))

        if i == "DeuterExtractor":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(225 * math.pow(1.5, lvl - 1)))
                    result.add("crystal", math.floor(75 * math.pow(1.5, lvl - 1)))
                    result.add("energy", math.ceil(20 * lvl * math.pow(1.1, lvl)))

        if i == "SolarPowerPlant":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(75 * math.pow(1.5, lvl - 1)))
                    result.add("crystal", math.floor(30 * math.pow(1.5, lvl - 1)))

        if i == "FusionPowerPlant":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(75 * math.pow(1.5, lvl - 1)))
                    result.add("crystal", math.floor(30 * math.pow(1.5, lvl - 1)))

        if i == "MetalStorage":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(1000 * math.pow(2, lvl - 1)))


        if i == "CrystalStorage":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(1000 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(500 * math.pow(2, lvl - 1)))

        if i == "DeuterStorage":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(1000 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(1000 * math.pow(2, lvl - 1)))

        # Station Buildings

        if i == "RobotFactory":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(400 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(120 * math.pow(2, lvl - 1)))
                    result.add("deuter", math.floor(200 * math.pow(2, lvl - 1)))

        if i == "Shipyard":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(400 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(200 * math.pow(2, lvl - 1)))
                    result.add("deuter", math.floor(100 * math.pow(2, lvl - 1)))

        if i == "Laboratory":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(200 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(400 * math.pow(2, lvl - 1)))
                    result.add("deuter", math.floor(200 * math.pow(2, lvl - 1)))

        if i == "AllayDepot":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(20000 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(40000 * math.pow(2, lvl - 1)))

        if i == "RocketSilo":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(20000 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(20000 * math.pow(2, lvl - 1)))
                    result.add("deuter", math.floor(1000 * math.pow(2, lvl - 1)))

        if i == "NaniteFactory":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(1000000 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(500000 * math.pow(2, lvl - 1)))
                    result.add("deuter", math.floor(100000 * math.pow(2, lvl - 1)))

        if i == "Terraformer":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("crystal", math.floor(500000 * math.pow(2, lvl - 1)))
                    result.add("deuter", math.ceil(100000 * math.pow(2, lvl - 1)))
                # you need just max energy so we add it once
                result.add("energy", math.floor(1000 * math.pow(2, wanted_state.get(i) - 1)))

        if i == "SpaceDock":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(200 * math.pow(5, lvl - 1)))
                    result.add("deuter", math.floor(50 * math.pow(5, lvl - 1)))
                # you need just max energy so we add it once
                result.add("energy", math.floor(50 * math.pow(5, wanted_state.get(i) - 1)))

        # Research

        if i == "EnergyTechnology":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("crystal", math.floor(800 * math.pow(2, lvl - 1)))
                    result.add("deuter", math.floor(400 * math.pow(2, lvl - 1)))

        if i == "LaserTechnology":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(200 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(100 * math.pow(2, lvl - 1)))

        if i == "IonTechnology":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(1000 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(300 * math.pow(2, lvl - 1)))
                    result.add("deuter", math.floor(100 * math.pow(2, lvl - 1)))

        if i == "HyperspaceTechnology":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("crystal", math.floor(4000 * math.pow(2, lvl - 1)))
                    result.add("deuter", math.floor(2000 * math.pow(2, lvl - 1)))

        if i == "PlasmaTechnology":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(2000 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(4000 * math.pow(2, lvl - 1)))
                    result.add("deuter", math.floor(1000 * math.pow(2, lvl - 1)))

        if i == "CombustionDrive":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(400 * math.pow(2, lvl - 1)))
                    result.add("deuter", math.floor(600 * math.pow(2, lvl - 1)))

        if i == "ImpulseDrive":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(2000 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(4000 * math.pow(2, lvl - 1)))
                    result.add("deuter", math.floor(600 * math.pow(2, lvl - 1)))

        if i == "HyperDrive":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(10000 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(20000 * math.pow(2, lvl - 1)))
                    result.add("deuter", math.floor(6000 * math.pow(2, lvl - 1)))

        if i == "SpyTechnology":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(200 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(1000 * math.pow(2, lvl - 1)))
                    result.add("deuter", math.floor(200 * math.pow(2, lvl - 1)))

        if i == "ComputerTechnology":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("crystal", math.floor(400 * math.pow(2, lvl - 1)))
                    result.add("deuter", math.floor(600 * math.pow(2, lvl - 1)))

        if i == "Astrophysics":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", 100 * math.floor(40 * math.pow(1.75, lvl - 1)))
                    result.add("crystal", 100 * math.floor(80 * math.pow(1.75, lvl - 1)))
                    result.add("deuter", 100 * math.floor(40 * math.pow(1.75, lvl - 1)))

        if i == "IntergalacticResearchNetwork":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(240000 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(400000 * math.pow(2, lvl - 1)))
                    result.add("deuter", math.floor(160000 * math.pow(2, lvl - 1)))

        if i == "GravitonDevelopment":
            if wanted_state.get(i) > current_state.get(i):
                result.add("energy", 300000 * math.pow(3, wanted_state.get(i) - 1))

        if i == "BattleTechnology":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(800 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(200 * math.pow(2, lvl - 1)))

        if i == "ShieldingTechnology":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(200 * math.pow(2, lvl - 1)))
                    result.add("crystal", math.floor(600 * math.pow(2, lvl - 1)))

        if i == "Armor":
            if wanted_state.get(i) > current_state.get(i):
                for lvl in range(current_state.get(i) + 1, wanted_state.get(i) + 1):
                    result.add("metal", math.floor(1000 * math.pow(2, lvl - 1)))

        # Ships

        if i == "LightFighter":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 3000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 1000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "HeavyFigher":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 6000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 4000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "Cruiser":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 20000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 7000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("deuter", 2000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "Battleship":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 45000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 15000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "LightTransport":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 2000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 2000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "HeavyTransport":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 6000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 6000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "ColonizationShip":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 10000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 20000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("deuter", 10000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "Dreadnought":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 30000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 40000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("deuter", 15000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "Bomber":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 50000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 25000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("deuter", 15000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "Destroyer":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 60000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 50000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("deuter", 15000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "DeathStar":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 5000000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 4000000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("deuter", 1000000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "Recycler":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 10000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 6000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("deuter", 2000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "SpyProbe":
            if wanted_state.get(i) > current_state.get(i):
                result.add("crystal", 1000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "SolarSatellite":
            if wanted_state.get(i) > current_state.get(i):
                result.add("crystal", 2000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("deuter", 500 * (wanted_state.get(i) - current_state.get(i)))

        # Defenses

        if i == "RocketLauncher":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 2000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "LightLaserCannon":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 1500 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 500 * (wanted_state.get(i) - current_state.get(i)))

        if i == "HeavyLaserCannon":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 6000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 2000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "GaussCannon":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 20000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 15000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("deuter", 2000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "IonCannon":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 2000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 6000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "PlasmaLauncher":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 50000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 50000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("deuter", 30000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "SmallPlanetaryShield":
            if wanted_state.get(i) == 1 and current_state.get(i) == 0:
                result.add("metal", 10000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 10000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "LargePlanetaryShield":
            if wanted_state.get(i) == 1 and current_state.get(i) == 0:
                result.add("metal", 50000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 50000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "AntiMissile":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 8000 * (wanted_state.get(i) - current_state.get(i)))
                result.add("deuter", 2000 * (wanted_state.get(i) - current_state.get(i)))

        if i == "InterplanetaryMissile":
            if wanted_state.get(i) > current_state.get(i):
                result.add("metal", 12500 * (wanted_state.get(i) - current_state.get(i)))
                result.add("crystal", 2500 * (wanted_state.get(i) - current_state.get(i)))
                result.add("deuter", 10000 * (wanted_state.get(i) - current_state.get(i)))

    return result


class Requirements(PlanetState):
    def __init__(self):
        super(Requirements, self).__init__()
        self._attributes.append("time")
        setattr(self, self._attributes[-1], 0)
