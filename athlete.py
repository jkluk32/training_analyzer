print("--- Initializing Athlete System ---\n")

class Athlete:

    def __init__(self, name, ftp, weight_kg):

        self.name = name
        self.ftp = ftp
        self.weight_kg = weight_kg

    def calculate_watts_per_kg(self):
        wkg = self.ftp / self.weight_kg
        return round (wkg, 2)
    
if __name__ == "__main__":
    
    rider_one = Athlete("Alex", 285, 75.0)
    rider_two = Athlete("Sarah", 240, 58.5)

    print(f"{rider_one.name} has an FTP of {rider_one.ftp}W.")
    print(f"Alex's Power-To-Weight ratio is: {rider_one.calculate_watts_per_kg()} W/kg")

    print("\n-----------------\n")

    print(f"{rider_two.name} has an FTP of {rider_two.ftp}W.")
    print(f"Sarah's Powere-To-weight ratio is: {rider_two.calculate_watts_per_kg()} W/kg")