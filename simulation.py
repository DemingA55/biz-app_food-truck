import random
import matplotlib.pyplot as plt

# Number of days to simulate for each prep plan.
TRIALS = 1000

# Maximum acceptable average of missed units per day.
MAX_AVG_MISSED = 5

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


# Simulates one day of food truck demand.
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


# Calculates average leftovers and missed units over many days.
def average_day(prep_amounts, trials):
    """Return average leftover and missed units per simulated day."""
    total_leftovers = 0
    total_missed = 0

    for day in range(trials):
        leftovers, missed = simulate_day(prep_amounts)
        total_leftovers += leftovers
        total_missed += missed

    return total_leftovers / trials, total_missed / trials


# Shows and saves the average leftovers chart.
def save_simulation_chart(results):
    """Show a bar chart and save it after the preview closes."""
    plan_names = []
    average_leftovers = []

    for plan_name in results:
        plan_names.append(plan_name)
        average_leftovers.append(results[plan_name][0])

    for step in ["preview", "save"]:
        plt.figure()
        plt.bar(plan_names, average_leftovers)
        plt.title("Average Leftovers by Prep Plan")
        plt.xlabel("Prep Plan")
        plt.ylabel("Average Leftover Units per Day")

        if step == "preview":
            plt.show()
        else:
            plt.savefig("simulation_results.png")
            plt.close()


# Compares prep plans and recommends one.
def run_simulation():
    """Compare the prep plans and recommend one that meets the demand target."""
    results = {}

    for plan_name, prep_amounts in PREP_OPTIONS.items():
        results[plan_name] = average_day(prep_amounts, TRIALS)

    print(f"\nSimulated {TRIALS} days per prep plan.")
    print(f"{'Prep Plan':<12}{'Avg Leftovers/Day':>20}{'Avg Missed/Day':>18}")

    recommended_plan = ""
    best_leftovers = 0

    for plan_name, (avg_leftovers, avg_missed) in results.items():
        print(f"{plan_name:<12}{avg_leftovers:>20.2f}{avg_missed:>18.2f}")

        if avg_missed <= MAX_AVG_MISSED:
            if recommended_plan == "" or avg_leftovers < best_leftovers:
                recommended_plan = plan_name
                best_leftovers = avg_leftovers

    if recommended_plan == "":
        print(f"\nNo plan met the target of {MAX_AVG_MISSED} missed units per day.")
    else:
        print(f"\nRecommendation: Use the {recommended_plan} prep plan.")
    
    save_simulation_chart(results)
    print("\nSimulation chart saved to simulation_results.png.")




