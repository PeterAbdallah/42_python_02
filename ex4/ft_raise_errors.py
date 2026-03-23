#!/usr/bin/env python3

class InvalidNameError(Exception):
    pass


class WaterLevelError(Exception):
    pass


class SunlightHoursError(Exception):
    pass


def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    try:
        if not plant_name:
            raise InvalidNameError("Plant name cannot be empty!")

        if (water_level > 10):
            raise WaterLevelError(f"Water level {water_level} is too high\
 (max 10)")
        elif (water_level < 1):
            raise WaterLevelError(f"Water level {water_level} is too low\
 (min 1)")

        if (sunlight_hours > 12):
            raise SunlightHoursError(f"Sunlight hours {sunlight_hours} is too\
 high (max 12)")
        elif (sunlight_hours < 2):
            raise SunlightHoursError(f"Sunlight hours {sunlight_hours} is too\
 low (min 2)")
        print(f"Plant {plant_name} is healthy!")
    except InvalidNameError as e:
        print(f"Error: {e}")
    except WaterLevelError as e:
        print(f"Error: {e}")
    except SunlightHoursError as e:
        print(f"Error: {e}")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    check_plant_health("tomato", 2, 5)
    print("\nTesting empty plant name...")
    check_plant_health("", 2, 5)
    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 5)
    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 2, 0)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
