#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(plant_name: str, plant_health: str):
    if (plant_health == "wilting"):
        raise PlantError(f"The {plant_name} plant is wilting!")


def check_water(tank_level: int):
    if (tank_level < 1):
        raise WaterError("Not enough water in the tank!")


def ft_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    # PlantError
    print("\nTesting PlantError...")
    try:
        check_plant("tomato", "wilting")
    except PlantError as e:
        print("Caught PlantError: ", e)

    # WaterError
    print("\nTesting WaterError...")
    try:
        check_water(0)
    except WaterError as e:
        print("Caught WaterError: ", e)

    # GardenError
    print("\nTesting catching all garden errors...")
    try:
        check_plant("tomato", "wilting")
    except GardenError as e:
        print("Caught a garden error: ", e)
    try:
        check_water(0)
    except GardenError as e:
        print("Caught a garden error: ", e)

    print("\nAll custom error types work cprrectly!")


if __name__ == "__main__":
    ft_custom_errors()
