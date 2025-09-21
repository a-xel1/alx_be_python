task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task", end="")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task", end="")
    case "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.", end="")
    case _:
        print(f"Reminder: '{task}' has an unknown priority", end="")

if time_bound == "yes" and priority in ["high", "medium"]:
    print(" that requires immediate attention today!")
else:
    print()
