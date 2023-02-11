days_of_week = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
schedule = {}


def add_schedule(day, task):
    if day in schedule:
        schedule[day].append(task)
    else:
        schedule[day] = [task]


print("Enter your schedules for each day of the week, or type 'done' when finished.")

while True:
    day = input("Enter day of the week: ")
    if day.lower() == 'done':
        break
    if day not in days_of_week:
        print("Invalid day of the week. Please try again.")
        continue
    task = input("Enter schedule: ")
    add_schedule(day, task)
print(".................................................")
print("\nHere is your schedule:")
for day in days_of_week:
    print(f"{day}:")
    if day in schedule:
        for task in schedule[day]:
            print(f"\t{task}")
    else:
        print("\tNo schedule")

print("...................................................")
