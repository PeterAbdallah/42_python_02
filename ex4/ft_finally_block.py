#!/usr/bin/env python3

class PlantError(Exception):
    pass


def water_plant(plant_name: str) -> None:
    if plant_name != str.capitalize(plant_name):
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    print("Opening watering system")
    try:
        for plant in ["Tomato", "Lettuce", "Carrots"]:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("...ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Opening watering system")
    try:
        for plant in ["Tomato", "lettuce", "Carrots"]:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("...ending tests and returning to main")
    finally:
        print("Closing watering system")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
