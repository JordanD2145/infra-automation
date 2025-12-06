import json
import sys
import os

# Add the project root directory to sys.path to allow imports from src
# This fixes "ModuleNotFoundError" when running from different folders
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import our custom modules
from src.machine import Machine
from src.logger import logger

def get_user_input():
    """
    Collects machine details from the user via the command line interface (CLI).
    Returns a list of machine dictionaries.
    """
    machines_list = []
    print("--- Welcome to Infra Automation ---")
    
    while True:
        # Ask the user for input
        name = input("Enter machine name (or type 'done' to finish): ")
        
        # Check if the user wants to exit
        if name.lower() == 'done':
            break
            
        # Collect the rest of the machine details
        os_type = input("Enter OS (e.g., Ubuntu, CentOS): ")
        cpu = input("Enter CPU (e.g., 2vCPU): ")
        ram = input("Enter RAM (e.g., 4GB): ")
        
        # Create a new Machine object using our Class from machine.py
        new_machine = Machine(name, os_type, cpu, ram)
        
        # Convert the object to a dictionary and add it to our list
        machines_list.append(new_machine.to_dict())
        print(f"✅ Machine '{name}' added successfully!\n")

    return machines_list

def save_to_file(data):
    """
    Saves the collected machine data to a JSON file in the 'configs' directory.
    """
    # Define the path: configs/instances.json
    filename = os.path.join('configs', 'instances.json')
    
    try:
        # Open the file in 'write' mode ('w'). Creates it if it doesn't exist.
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
            
        print(f"\n[V] Configuration saved successfully to: {filename}")
        logger.info(f"Configuration saved to {filename}")
        
    except Exception as e:
        # Handle any errors that occur during saving
        print(f"[X] Error saving file: {e}")
        logger.error(f"Failed to save file: {e}")

# --- Main Entry Point ---
# This block runs only if we execute this file directly
if __name__ == "__main__":
    logger.info("System started")
    
    # Step 1: Get input from the user
    collected_data = get_user_input()
    
    # Step 2: Save data if machines were created
    if collected_data:
        save_to_file(collected_data)
    else:
        print("No machines created. Exiting.")