########

# Implement Class

########
class Implement:
    def __init__(self, implement_type):
        # Initialize a new Implement instance with implement_type
        self.implement_id = id(self)
        self.type = implement_type

    def get_filling_type(self):
        # If the type of the implement is Sprayer, return the type of the filling (water or pesticides)
        if self.type == "Sprayer":
            return "water" if "water" in self.type.lower() else "pesticides"
        return None