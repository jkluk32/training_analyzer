from models.athlete import Athlete
from models.workout import Workout

print("--- Calculating Weekly Training Load ---\n")

sarah = Athlete("Sarah", 240, 58.5)

sarahs_week = [
    Workout("Monday Recovery", 45, 130),
    Workout("Tuesday Intervals", 90, 205),
    Workout("Thursday Sweet Spot", 60, 215),
    Workout("Saturday Long Ride", 180, 160)
]

total_weekly_tss = 0

print(f"Training Log for: {sarah.name}\n")

for ride in sarahs_week:

    daily_score = ride.calculate_tss(sarah)

    print(f"{ride.title}: {daily_score} TSS")

    total_weekly_tss+= daily_score

print("\n-----------------------")
print(f"Total Weekly TSS: {round(total_weekly_tss, 1)}")