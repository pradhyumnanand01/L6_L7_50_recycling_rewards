
import math


def parse_collection(text):
    if not isinstance(text, str) or text.count(':') != 1:
        raise ValueError("Input must be in material:weight format")

    material, kg = text.split(':')
    material = material.strip()

    if not material:
        raise ValueError("Material cannot be empty")

    try:
        weight = float(kg)
    except (ValueError, TypeError):
        raise ValueError("Weight must be numeric")

    if not math.isfinite(weight) or weight < 0:
        raise ValueError("Weight must be finite and non-negative")

    return material.title(), weight


def weight_average(weights_csv):
    if not isinstance(weights_csv, str) or not weights_csv.strip():
        raise ValueError("Weights cannot be empty")

    try:
        values = [float(r.strip()) for r in weights_csv.split(',')]
    except (ValueError, TypeError):
        raise ValueError("All weights must be numeric")

    if not values or any(not math.isfinite(v) or v < 0 for v in values):
        raise ValueError("Weights must be finite and non-negative")

    return sum(values) // len(values)


def net_points(text):
    if not isinstance(text, str) or text.count('|') != 1:
        raise ValueError("Input must be in points|penalty format")

    points, penalty = text.split('|')

    try:
        points = float(points)
        penalty = float(penalty)
    except (ValueError, TypeError):
        raise ValueError("Points and penalty must be numeric")

    if not math.isfinite(points) or not math.isfinite(penalty):
        raise ValueError("Points and penalty must be finite")

    if points < 0 or penalty < 0:
        raise ValueError("Points and penalty cannot be negative")

    total = points * 2 - penalty
    return max(total, 0)


def main():
    print("==== Running parse_collection ====")
    user_input = input("Enter material:weight in kg (e.g. paper:12): ")
    print("Material and Weight:", parse_collection(user_input))

    print("\n==== Running weight_average ====")
    user_input = input("Enter weights in kg as CSV (e.g. 5,12,20): ")
    print("Average Weight:", weight_average(user_input))

    print("\n==== Running net_points ====")
    user_input = input("Enter points|penalty (e.g. 80|10): ")
    print("Net Points:", net_points(user_input))


if __name__ == "__main__":
    main()
