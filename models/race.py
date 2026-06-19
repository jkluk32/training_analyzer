from models.athlete import Athlete
from models.workout import Workout

print("--- Initializing Race System ---\n")

class Race(Workout):
    
    def __init__(self, title, duration_minutes, avg_watts, placement):

        super().__init__(title, duration_minutes, avg_watts)

        self.placement = placement

    def podium_check(self):
        if self.placement <= 3:
            return "PODIUM FINISH!"
        else:
            return "Solid effort, back to training."
        
if __name__ == "__main__":

    sarah = Athlete("Sarah", 240, 58.5)

    sunday_crit = Race("Downtown Criterium", 45, 230, 2)

    print(f"Event: {sunday_crit.title}")
    print(f"Result: {sunday_crit.placement}nd Place - {sunday_crit.podium_check()}")

    race_tss = sunday_crit.calculate_tss(sarah)
    print(f"TSS Earned: {race_tss}")