import datetime
import math
import random
import uuid


def explore_modules():
    modules = {
        "1": ("datetime", datetime),
        "2": ("math", math),
        "3": ("random", random),
        "4": ("uuid", uuid),
    }

    print("\n--- EXPLORE MODULE ATTRIBUTES (dir()) ---")
    for key, (name, module) in modules.items():
        print(f"{key}. {name}")

    choice = input("Choose a module to explore: ").strip()
    if choice not in modules:
        print("Invalid module choice.")
        return

    name, module = modules[choice]
    print(f"\nAttributes available in {name} module:")
    attributes = dir(module)
    print(", ".join(attributes))
    print(f"\nTotal attributes: {len(attributes)}")
