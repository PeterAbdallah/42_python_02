#!/usr/bin/env python3

class Plant():
    def __init__(self, name: str):
        self.name = name


def water_plants(plant_list: list[Plant]):
    print("Opening Watering system")
    try:
        for plant in plant_list:
            if not isinstance(plant, Plant):
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant.name}")
        print("Watering completed successfully!")
    except ValueError as e:
        print("Error: ", e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")
    p1 = Plant("tomato")
    p2 = Plant("lettuce")
    p3 = Plant("carrots")
    good_list = [p1, p2, p3]
    bad_list = [p1, None, p3]

    print("\nTesting normal watering...")
    water_plants(good_list)
    print("\nTesting with error...")
    water_plants(bad_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
