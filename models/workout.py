from models.athlete import Athlete

class Workout:
    def __init__(self, title, duration_minutes, avg_watts):
        self.title = title
        self.duration_minutes = duration_minutes
        self.avg_watts = avg_watts

    def calculate_tss(self, rider):
        intensity = self.avg_watts / rider.ftp
        hours = self.duration_minutes / 60

        tss = (hours * (intensity ** 2)) * 100
        return round(tss, 1)

if __name__ == "__main__":

    rider_two = Athlete("Sarah", 240, 58.5)
    tuesday_ride = Workout("Tempo Intervals", 90, 205)

    sarah_score = tuesday_ride.calculate_tss(rider_two)

    print(f"Workout: {tuesday_ride.title}")
    print(f"Rider: {rider_two.name}")
    print(f"TSS Earned: {sarah_score}")