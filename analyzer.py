import pandas as pd
import matplotlib.pyplot as plt
from models.athlete import Athlete
from models.workout import Workout

print("--- Booting up Training Analyzer Engine ---\n")

class TrainingAnalyzer:
   
    def __init__(self, athlete):
        self.athlete = athlete
        self.workout_list = []

    def load_data_from_csv(self, filename):
        df = pd.read_csv(filename)
        for index, row in df.iterrows():

            new_ride = Workout(row["Title"], row["Duration"], row["Watts"])
            self.workout_list.append(new_ride)

        print(f"Successfully loaded {len(self.workout_list)} rides from {filename}. \n")

    def calculate_total_load(self):
        total_tss = 0
        for ride in self.workout_list:
            total_tss += ride.calculate_tss(self.athlete)
        return round(total_tss, 1)
    
    def plot_weekly_stress(self):
        workout_names = []
        tss_scores = []

        for ride in self.workout_list:
            workout_names.append(ride.title)
            tss_scores.append(ride.calculate_tss(self.athlete))

        plt.bar(workout_names, tss_scores, color="royalblue")
        plt.title(f"Weekly Training Stress for {self.athlete.name}")
        plt.xlabel("Workout")
        plt.ylabel("TSS")

        plt.xticks(rotation=15)

        print("Rendering visual graph... (Close the pop-up window to end the script)")
        plt.tight_layout()
        fig = plt.gcf()
        return fig

if __name__ == "__main__":
    sarah = Athlete("Sarah", 240, 58.5)
    app = TrainingAnalyzer(sarah)
    app.load_data_from_csv("data/ride_data.csv")

    final_score = app.calculate_total_load()
    print(f"Total Weekly Training Stress for {sarah.name}: {final_score} TSS")

    app.plot_weekly_stress()