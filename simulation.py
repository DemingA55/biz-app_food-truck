import random

# Minimum and maximum daily demand for each menu item.
DEMAND_RANGES = {
    "Taco": (15, 35),
    "Burrito": (10, 25),
    "Quesadilla": (12, 30),
    "Salad": (7, 18),
    "Cookie": (20, 48),
}

# Number of units prepared per item for each daily prep plan.
PREP_OPTIONS = {
    "Light": {
        "Taco": 24,
        "Burrito": 16,
        "Quesadilla": 20,
        "Salad": 12,
        "Cookie": 32,
    },
    "Standard": {
        "Taco": 30,
        "Burrito": 20,
        "Quesadilla": 25,
        "Salad": 15,
        "Cookie": 40,
    },
    "Heavy": {
        "Taco": 36,
        "Burrito": 24,
        "Quesadilla": 30,
        "Salad": 18,
        "Cookie": 48,
    },
}


def simulate_day(prep_amounts):
    """Simulate one day and return total leftovers and missed units."""
    leftovers = 0
    missed_units = 0

    for item, prepared in prep_amounts.items():
        minimum_demand, maximum_demand = DEMAND_RANGES[item]
        demand = random.randint(minimum_demand, maximum_demand)
        sold = min(prepared, demand)

        leftovers += prepared - sold
        missed_units += demand - sold

    return leftovers, missed_units