import time

########

# Tractor Class

########
class Tractor:
    def __init__(self, tractor_type):
        # Initialize a new Tractor instance with tractor_type and other default attributes
        self.tractor_id = id(self)
        self.tractor_type = tractor_type
        self.fuel_status = 100
        self.implement = None
        self.status = "Off"
        self.done_work_percentage = 0.0
    
    def is_working(self):
        # Check if the tractor is currently working
        return self.status == "Working"
    
    def turn_on(self):
        # Turn on the tractor if it's currently off
        if self.status == "Off":
            self.status = "On"
            print(f"Tractor {self.tractor_id} is turned on.")
    
    def turn_off(self):
        # Turn off the tractor if it's currently on
        if self.status == "On":
            self.status = "Off"
            print(f"Tractor {self.tractor_id} is turned off.")
    
    def run(self):
        # Start the tractor and simulate its operation while decrementing fuel status
        if self.status == "Off":
            print(f"Tractor {self.tractor_id} cannot run. Turn it on first.")
            return
        
        self.status = "Working"
        while self.fuel_status > 0:
            time.sleep(1)
            self.fuel_status -= 1
            self.done_work_percentage += 1
            print(f"Tractor {self.tractor_id} running. Fuel: {self.fuel_status}%")
            if self.fuel_status <= 10:
                print(f"Tractor {self.tractor_id} has only {self.fuel_status}% fuel left. Please refuel.")
                break
        
        self.status = "Stopped"
        print(f"Tractor {self.tractor_id} stopped. Done work: {self.done_work_percentage:.2f}%")
    
    def stop(self):
        # Stop the tractor and change its status to Stopped
        self.status = "Stopped"
        print(f"Tractor {self.tractor_id} stopped.")
    
    def attach_implement(self, implement):
        # Attach an implement to the tractor
        self.implement = implement
        print(f"Implement {self.implement.implement_id} attached to Tractor {self.tractor_id}.")
    
    def change_implement(self, new_implement):
        # Change the current implement of the tractor
        self.implement = new_implement
        print(f"Tractor {self.tractor_id} changed its implement to {self.implement.type}.")
