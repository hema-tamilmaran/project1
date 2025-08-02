import time
import random

def detect_banana():
    time.sleep(1)
    return True

def check_damage():
    return random.choice([True, False])

def detect_color():
    return random.choice(["yellow", "green"])

def peel_banana(color):
    print(f"🌀 Peeling {color} banana... Done.")

def route_banana(color):
    print(f"🔀 Routing banana to {color} path...")

def cut_banana(shape):
    print(f"🔪 Cutting banana into {shape} slices...")
    slices = 3 if shape == "thin" else 2
    for i in range(slices):
        print(f"  ✂ Slice {i + 1}")
        time.sleep(0.5)
    print("✅ Cutting complete.")

# MAIN
print("🍌 Welcome to Banana Peeler Simulator 🍌")

# Get input from user
try:
    total_bananas = int(input("👉 Enter number of bananas to process: "))
    slice_mode = input("👉 Enter slicing style (thin / medium/avarage): ").strip().lower()
    if slice_mode not in ["thin", "medium","avarage"]:
        print("⚠ Invalid input. Defaulting to 'thin' slicing.")
        slice_mode = "thin"

    print("\n✅ Starting the process...\n")
    for count in range(1, total_bananas + 1):
        if detect_banana():
            print(f"\n🔍 [Banana #{count}] detected")

            if check_damage():
                print("❌ Damage detected. Banana removed.")
                continue

            color = detect_color()
            print(f"🎨 Color detected: {color}")

            peel_banana(color)
            route_banana(color)
            cut_banana(slice_mode)

            time.sleep(1)

    print("\n🏁 All bananas processed. Thank you!")
except ValueError:
    print("❌ Invalid input. Please enter a valid number.")
except KeyboardInterrupt:
    print("\n🛑 Simulation stopped by user.")