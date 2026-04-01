#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(plant_name: str, plant_health: str) -> None:
    if (plant_health == "wilting"):
        raise PlantError(f"The {plant_name} plant is wilting!")


def check_water(tank_level: int) -> None:
    if (tank_level < 1):
        raise WaterError("Not enough water in the tank!")


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    # PlantError
    print("\nTesting PlantError...")
    try:
        check_plant("tomato", "wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    # WaterError
    print("\nTesting WaterError...")
    try:
        check_water(0)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    # GardenError
    print("\nTesting catching all garden errors...")
    try:
        check_plant("tomato", "wilting")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water(0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
