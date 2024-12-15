# Import libraries
import random

# Days of the month (4 weeks from Monday to Friday)
days = [
    "Miercoles_8", "Jueves_9", "Viernes_10",
    "Lunes_13", "Miercoles_15", "Jueves_16", "Viernes_17",
    "Lunes_20", "Miercoles_22", "Jueves_23", "Viernes_24",
    "Lunes_27", "Miercoles_29", "Jueves_30"
]

# Teachers and their availability
teachers = {
    "Andrea": days,  # Available all days
    "Arancha": days,  # Available all days
    "Elena": days,  # Available all days
    "Esther": [d for d in days if "Lunes" not in d],  # Not available on Mondays
    "Juanra": days,  # Available all days
    "Loreto": [d for d in days if "Lunes" in d or "Miercoles" in d],  # Prefers Mondays or Wednesdays
    "Lucia": [d for d in days if "Miercoles" in d or "Viernes" in d],  # Prefers Wednesdays or Fridays
    "Luisa": days,  # Available all days
    "Mariano": days,  # Available all days
    "Marta": days,  # Available all days
    "Ricardo": days,  # Available all days
    "Yanina": [days[i] for i in range(len(days)) if (i // 5) % 2 == 0],  # Available every two weeks
}

# Initialize the counter for assignments per teacher
guard_count = {teacher: 0 for teacher in teachers}

# Create a dictionary to store the assignments per teacher
schedule_by_teacher = {teacher: [] for teacher in teachers}

# Round control
round_number = 0
teachers_per_round = list(teachers.keys())  # Initialize the list of teachers per round

# Assign guards
for day in days:
    # Increment the round after completing one rotation
    if len(teachers_per_round) == 0:
        round_number += 1
        teachers_per_round = list(teachers.keys())  # Reset the teacher list for the new round

    # Filter teachers available for the day
    available = [t for t in teachers if any(day.startswith(d.split("_")[0]) for d in teachers[t])]

    # Apply restriction for Loreto and Yanina: only in even rounds
    if round_number % 2 == 1:  # Odd rounds
        available = [t for t in available if t not in {"Loreto", "Yanina"}]

    # Shuffle available teachers randomly
    random.shuffle(available)

    if not available:
        print(f"No teachers available for {day}.")
        continue

    # Select the teacher with the least number of assignments
    selected_teacher = min(available, key=lambda t: guard_count[t])

    # Assign the day to the teacher
    schedule_by_teacher[selected_teacher].append(day)
    guard_count[selected_teacher] += 1

    # Remove the selected teacher from the current round
    if selected_teacher in teachers_per_round:
        teachers_per_round.remove(selected_teacher)

# Display the schedule by teacher
print("Guard schedule by teacher:")
for teacher, assigned_days in schedule_by_teacher.items():
    print(f"{teacher}: {', '.join(assigned_days)}")

# Display the total guard distribution
print("\nGuard distribution:")
for teacher, total in guard_count.items():
    print(f"{teacher}: {total} guards")
