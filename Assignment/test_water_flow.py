# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2000000  # kg/m³
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pa·s

# Function: pressure_loss_from_fittings
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calculates the pressure loss due to fittings.
    """
    pressure_loss = -0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings / 2000
    return pressure_loss

# Function: reynolds_number
def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculates the Reynolds number.
    """
    reynolds = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return reynolds

# Function: pressure_loss_from_pipe_reduction
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculates the pressure loss from pipe reduction.
    """
    diameter_ratio = (larger_diameter / smaller_diameter) ** 4
    k = 0.1 + (50 / reynolds_number) * (diameter_ratio - 1)
    pressure_loss = -k * WATER_DENSITY * fluid_velocity**2 / 2000
    return pressure_loss

# Conversion function: kPa to psi
def kpa_to_psi(kpa):
    """
    Converts pressure from kilopascals (kPa) to pounds per square inch (psi).
    """
    return kpa * 0.145038

# Main program
def main():
    """
    Main function to calculate the water pressure at the house.
    """
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    # Example calculations using existing functions (integrate additional functions as needed)
    water_height = tower_height + tank_height
    pressure = water_height * WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY / 1000

    # Adjust calculations based on pipe dimensions and fittings
    velocity = 1.65  # Supply velocity
    loss_from_fittings = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss_from_fittings

    print(f"Pressure at house: {pressure:.2f} kPa ({kpa_to_psi(pressure):.2f} psi)")

if __name__ == "__main__":
    main()

