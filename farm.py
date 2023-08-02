########

# Farm Class

########
class Farm:
    def __init__(self, name, farm_type, location):
        # Initialize a new Farm instance with name, farm_type, and location attributes
        self.name = name
        self.farm_type = farm_type
        self.location = location
        self.tractors_assigned = []
    
    def generate_farm_id(self):
        # Generate a unique farm ID based on the name and location on the map
        return f"{self.name}_{self.location['x']}_{self.location['y']}"
    
    def get_working_tractors(self):
        # Return a list of tractors that are currently working on the farm
        return [tractor for tractor in self.tractors_assigned if tractor.is_working()]
    
    def get_implement_by_season(self, season):
        # Return the correct type of Implement depending on the season
        if season == "summer":
            return "Sprayer filled with water"
        elif season == "fall":
            return "Mower"
        elif season == "winter":
            return "Driller"
        elif season == "spring":
            return "Sprayer filled with pesticides"

    def list_tractors_status(self):
        # Create a list of dictionaries containing tractor statuses with their attributes
        tractor_statuses = []
        for tractor in self.tractors_assigned:
            tractor_statuses.append(
                {
                    "Tractor Type": tractor.tractor_type,
                    "Tractor Status": tractor.status,
                    "Implement": tractor.implement.type if tractor.implement else "None",
                    "Done Work Percentage": f"{tractor.done_work_percentage:.2f}%"
                }
            )
        return tractor_statuses

