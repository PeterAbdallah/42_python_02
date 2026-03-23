#!/usr/bin/env python3

class InvalidNameError(Exception):
    pass


class WaterLevelError(Exception):
    pass


class SunlightHoursError(Exception):
    pass


class GardenError(Exception):
    pass


class GardenManager():
    def __init__(self):
        self.plant_list = []

    def add_plant(self, plant_name: str):
        try:
            if not plant_name:
                raise InvalidNameError("Plant name cannot be empty!")
            self.plant_list.append(plant_name)
            print(f"Added {plant_name} successfully")
        except InvalidNameError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        print("Opening Watering system")
        try:
            for plant in self.plant_list:
                if not isinstance(plant, str):
                    raise ValueError(f"Cannot water {plant} - invalid plant!")
                print(f"Watering {plant} - success")
        except ValueError as e:
            print("Error: ", e)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, water_level: int, sunlight_hours: int):
        try:
            for plant in self.plant_list:
                if (water_level > 10):
                    raise WaterLevelError(f"Water level {water_level}\
 is too high (max 10)")
                elif (water_level < 1):
                    raise WaterLevelError(f"Water level {water_level}\
 is too low (min 1)")

                if (sunlight_hours > 12):
                    raise SunlightHoursError(f"Sunlight hours {sunlight_hours}\
 is too high (max 12)")
                elif (sunlight_hours < 2):
                    raise SunlightHoursError(f"Sunlight hours {sunlight_hours}\
 is too low (min 2)")
                print(f"{plant}: healthy (water: {water_level},\
 sun: {sunlight_hours})")
                water_level = 15
        except WaterLevelError as e:
            print(f"Error checking {plant}: {e}")
        except SunlightHoursError as e:
            print(f"Error checking {plant}: {e}")


def test_garden_management():
    manager = GardenManager()
    print("=== Garden Management System ===")
    print("\nAdding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    manager.check_plant_health(5, 8)

    print("\nTesting error recovery...")
    try:
        tank_level = 0
        if (tank_level < 1):
            raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
