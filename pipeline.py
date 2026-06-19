import pandas as pd

print("--- Booting up Time-Series Engine ---\n")

class TimeSeriesWorkout:

    def __init__(self, title, filename):
        self.title = title
        try:
            self.raw_data = pd.read_csv(filename)
            self.is_valid = True
        except FileNotFoundError:
            print(f"CRITICAL ERROR: The file '{filename}' does not exist!")
            self.is_valid = False
            self.raw_data = None
    
    def get_peak_power(self):
        if self.is_valid == True:
            return self.raw_data["Watts"].max()
        else:
            return 0
    
    def get_avg_power(self):
        if self.is_valid == True:
            return round(self.raw_data["Watts"].mean(), 1)
        else:
            return 0
    
    def get_best_5sec_power(self):
        if self.is_valid == True:
            best_5sec = self.raw_data["Watts"].rolling(window=5).mean().max()
            return round(best_5sec,1)
        else:
            return 0
    
if __name__ == "__main__":

    town_sign_sprint = TimeSeriesWorkout("Town Sign Sprint", "ghost_data.csv")

    print(f"Workout: {town_sign_sprint.title}")
    print(f"Peak Power Hit: {town_sign_sprint.get_peak_power()}W")
    print(f"Average Power: {town_sign_sprint.get_avg_power()}W")
    print(f"Best 5 second power: {town_sign_sprint.get_best_5sec_power()}W")