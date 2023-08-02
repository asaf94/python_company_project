########

# Main Class

########

from farm import Farm
from tractor import Tractor
from implement import Implement

class Main:
    def __init__(self, farm_name, season):
        # Initialize a new Main instance with farm_name and season attributes
        self.farm = Farm(farm_name, "Apples", {"x": 10, "y": 20, "width": 100, "height": 200})
        self.season = season
    
    def run_farm_simulation(self):
        # Ask for the number of dedicated tractors and check if it's more than 3
        num_tractors = int(input("Enter the number of dedicated tractors (should be more than 3): "))
        if num_tractors < 3:
            print("Number of tractors should be more than 3.")
            return

        # Create tractor instances and assign them to the farm
        for _ in range(num_tractors):
            tractor_type = input(f"Enter the type of Tractor {_ + 1} (John Deere or New Holland): ")
            tractor = Tractor(tractor_type)
            self.farm.tractors_assigned.append(tractor)
        
        # Turn on all tractors before running
        for tractor in self.farm.tractors_assigned:
            tractor.turn_on()
        
        # Assign implements to the first 3 tractors and make them run
        for tractor in self.farm.tractors_assigned[:3]:
            implement_type = self.farm.get_implement_by_season(self.season)
            implement = Implement(implement_type)
            tractor.attach_implement(implement)
            tractor.run()
        
        # Continue with the remaining tractors if any
        for tractor in self.farm.tractors_assigned[3:]:
            if tractor.is_working():
                continue
            tractor.change_implement(self.farm.tractors_assigned[0].implement)
            tractor.run()
        
        # Turn off all tractors
        for tractor in self.farm.tractors_assigned:
            if tractor.is_working():
                tractor.stop()


if __name__ == "__main__":
    farm_name = input("Enter the name of the farm: ")
    season = input("Enter the season (winter, fall, summer, spring): ")
    main = Main(farm_name, season)
    main.run_farm_simulation()
