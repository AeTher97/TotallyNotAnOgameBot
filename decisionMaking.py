from planetState import PlanetState
from fleet import Fleet
from Requirements import getRequirementsTech
from Requirements import getRequirementsRes


def find_steps(old_state=PlanetState(), new_state=PlanetState()):
    """
    Priority:
    Buildings and researches needed for next activity
    Buildings that speed up other activities
    Researches
    Ships
    Defenses
    Mining Buildings
    Other Buildings
    SolarSatellites
    :param old_state: object PlanetState
    :param new_state: object PlanetState
    :return: list of objects PlanetState
    """
    steps_list = list()

    priority_list = [
        "RobotFactory",
        "Shipyard",
        "Laboratory",
        "NaniteFactory",

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

        'LightFighter', # 20 index
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

        'RocketLauncher',
        'LightLaserCannon',
        'HeavyLaserCannon',
        'GaussCannon',
        'IonCannon',
        'PlasmaLauncher',
        'SmallPlanetaryShield',
        'LargePlanetaryShield',
        'AntiMissile',
        'InterplanetaryMissile', # index 42

        "MetalMine",
        "CrystalMine",
        "DeuterExtractor",

        "SolarPowerPlant",
        "FusionPowerPlant",
        "MetalStorage",
        "CrystalStorage",
        "DeuterStorage",
        "AllayDepot",
        "RocketSilo",
        "Terraformer",
        "SpaceDock",

        'SolarSatellite'
        ]

    # if in new_state requirements for new_state aren't included, add them to new_state
    req = getRequirementsTech(new_state)
    if new_state >= req:
        pass
    else:
        for i in new_state._attributes:
            new_state.set_min(i, req.get(i))

    prev_step = old_state.copy()

    while not (prev_step >= new_state):
        for i in range(0, len(priority_list)):
            if prev_step.get(priority_list[i]) < new_state.get(priority_list[i]):
                test_state = prev_step.copy()

                if (20 <= i <= 42) or i == 55:
                    test_state.set(priority_list[i], new_state.get(priority_list[i]))
                else:
                    test_state.set(priority_list[i], test_state.get(priority_list[i]) + 1)
                if test_state >= getRequirementsTech(test_state):
                    prev_step = test_state
                    steps_list.append(prev_step.copy())
                    break
                else:
                    steps_list.extend(find_steps(prev_step, getRequirementsTech(test_state)))
                    prev_step = steps_list[-1]

    return steps_list


def convert_steps_to_orders(prev_state, list_of_steps):
    list_of_orders = list()
    for i in range(0, len(list_of_steps)):
        for j in list_of_steps[i]._attributes:
            if i == 0:
                if prev_state.get(j) != list_of_steps[i].get(j):
                    res_needed = getRequirementsRes(prev_state, list_of_steps[i])
                    list_of_orders.append(Order("gather", res_needed.get("metal"), res_needed.get("crystal"), res_needed.get("deuter")))
                    list_of_orders.append(Order("build", j, list_of_steps[i].get(j)))
            else:
                if list_of_steps[i - 1].get(j) != list_of_steps[i].get(j):
                    res_needed = getRequirementsRes(list_of_steps[i - 1], list_of_steps[i])
                    list_of_orders.append(Order("gather", res_needed.get("metal"), res_needed.get("crystal"), res_needed.get("deuter")))
                    list_of_orders.append(Order("build", j, list_of_steps[i].get(j)))
    return list_of_orders

def spy_raports_to_attack(spy_reports, max_attacks, useHeavyTransporters=False):
    threats = ['LightFighter',
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

    'RocketLauncher',
    'LightLaserCannon',
    'HeavyLaserCannon',
    'GaussCannon',
    'IonCannon',
    'PlasmaLauncher',
    'SmallPlanetaryShield',
    'LargePlanetaryShield',
    'AntiMissile',
    'InterplanetaryMissile']

    number_of_reports = len(spy_reports)
    potential_targets = list()

    # search for defensless targets
    for i in range(0, len(spy_reports)):
        defensless = True
        for j in threats:
            if spy_reports[i].get(j) > 0:
                defensless = False
                break
        if defensless:
            potential_targets.append(spy_reports[i])

    # search for best profit targets
    profit_list = list()
    for i in range(0, len(potential_targets)):
        profit = potential_targets[i].get("metal")
        profit += potential_targets[i].get("crystal")
        profit += potential_targets[i].get("deuter")
        profit_list.append((profit, i))

    profit_list.sort(key=lambda profit: profit[0], reverse=True)

    result = list()

    for i in range(0, len(profit_list)):
        if i + 1 > max_attacks:
            break
        attack_fleet = Fleet()
        if useHeavyTransporters:
            attack_fleet.set("HeavyTransport", int(profit_list[i][0]/50000))
        else:
            attack_fleet.set("LightTransport", int(profit_list[i][0]/10000))
        target_planet = potential_targets[profit_list[i][1]]
        result.append(Order("attack", attack_fleet, target_planet))

    return result

class Order:
    def __init__(self, _action, *args):
        self.action = _action

        try:
            if self.action == "build":
                self.thing = args[0]
                self.lvl = args[1]
            elif self.action == "gather":
                self.metal = args[0]
                self.crystal = args[1]
                self.deuter = args[2]
            elif self.action == "attack":
                self.fleet = args[0]
                self.target = args[1]
            else:
                raise AttributeError("There is no such action as: " + str(_action))
        except IndexError:
            raise AttributeError("Too few arguments")

    def __str__(self):
        result = ""
        if self.action == "build":
            result = self.action + " " + self.thing + " " + str(self.lvl)
        elif self.action == "gather":
            result = self.action + " " + str(self.metal) + " metal, " + str(self.crystal) + " crystal, " + str(self.deuter) + " deuter."
        elif self.action == "attack":
            result = self.action + " " + str(self.target.get("Galaxy")) + ":" + str(self.target.get("Star")) + ":" + str(self.target.get("Planet"))

        return result