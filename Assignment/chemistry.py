from Assignment.formula import parse_formula # type: ignore

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

def make_periodic_table():
    """Create and return a periodic table as a dictionary."""
    periodic_table_dict = {
        "H": ["Hydrogen", 1.00794],
        "He": ["Helium", 4.002602],
        "Li": ["Lithium", 6.941],
        "Be": ["Beryllium", 9.012182],
        "B": ["Boron", 10.811],
        "C": ["Carbon", 12.0107],
        "N": ["Nitrogen", 14.0067],
        "O": ["Oxygen", 15.9994],
        "F": ["Fluorine", 18.9984032],
        "Ne": ["Neon", 20.1797],
        # Add more elements as needed...
    }
    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the elements listed."""
    total_molar_mass = 0
    for symbol, quantity in symbol_quantity_list:
        if symbol in periodic_table_dict:
            atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
            total_molar_mass += atomic_mass * quantity
        else:
            raise ValueError(f"Unknown element: {symbol}")
    return total_molar_mass

def main():
    # Get user input
    formula = input("Enter the molecular formula of the sample: ")
    try:
        mass = float(input("Enter the mass in grams of the sample: "))
    except ValueError:
        print("Invalid mass entered. Please enter a numeric value.")
        return

    # Generate the periodic table
    periodic_table = make_periodic_table()

    # Parse the formula into a symbol-quantity list
    try:
        symbol_quantity_list = parse_formula(formula)
        print(f"Parsed formula: {symbol_quantity_list}")
    except Exception as e:
        print(f"Error parsing formula: {e}")
        return

    # Compute the molar mass of the molecule
    try:
        molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)
    except ValueError as e:
        print(e)
        return

    # Compute the number of moles in the sample
    number_of_moles = mass / molar_mass

    # Print the results
    print(f"Molar mass: {molar_mass:.5f} grams/mole")
    print(f"Number of moles: {number_of_moles:.5f}")

if __name__ == "__main__":
    main()
