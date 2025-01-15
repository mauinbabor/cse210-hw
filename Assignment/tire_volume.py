from datetime import datetime
import math

def calculate_tire_volume(width, aspect_ratio, diameter):
    volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter )) / 10**7
    return round(volume, 2)

def main():
    # Get user inputs
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60) : "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
    
    # Calculate the volume
    volume = calculate_tire_volume(width, aspect_ratio, diameter)
    print(f"The approximate volume is {volume} liters")
    
    # Get current date
    current_date = datetime.now().date()
    
    # Write to file
    with open("volumes.txt", "a") as file:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume}\n")

if __name__ == "__main__":
    main()

