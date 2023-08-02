########

# Running The Main Class Object 

########

from main import Main

if __name__ == "__main__":
    farm_name = input("Enter the name of the farm: ")
    season = input("Enter the season (winter, fall, summer, spring): ")
    main = Main(farm_name, season)
    main.run_farm_simulation()
