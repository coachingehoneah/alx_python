# Prompt the user to input a task description
task = input("Enter your task: ")

# Prompt the user for the task's priority (high, medium, low)
priority = input("Priority (high/medium/low): ").lower()

# Prompt the user to check if the task is time-bound (yes or no)
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Provide a customized reminder
print("Reminder:", reminder)
