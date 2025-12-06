import json
import sys
import os
import subprocess  # This is the library required to run Bash scripts 

# Setup path to import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.machine import Machine
from src.logger import logger

def get_user_input():
    """Collects machine details from the user."""
    machines_list = []
    print("--- Welcome to Infra Automation ---")
    
    while True:
        name = input("Enter machine name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
            
        os_type = input("Enter OS (e.g., Ubuntu, CentOS): ")
        cpu = input("Enter CPU (e.g., 2vCPU): ")
        ram = input("Enter RAM (e.g., 4GB): ")
        
        new_machine = Machine(name, os_type, cpu, ram)
        machines_list.append(new_machine.to_dict())
        print(f"✅ Machine '{name}' added successfully!\n")

    return machines_list

def save_to_file(data):
    """Saves data to JSON file."""
    filename = os.path.join('configs', 'instances.json')
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"\n[V] Configuration saved to: {filename}")
        logger.info(f"Configuration saved to {filename}")
    except Exception as e:
        print(f"[X] Error saving file: {e}")
        logger.error(f"Failed to save file: {e}")

def run_setup_script():
    """
    Executes the Bash script using Python's subprocess module.
    Required by project instructions.
    """
    # Define the path to the script
    script_path = os.path.join('scripts', 'setup_nginx.sh')
    
    print(f"\n[INFO] Python is now running the Bash script: {script_path}...")
    logger.info(f"Starting execution of {script_path}")

    try:
        # This is the critical line: Python calls Bash to run the script
        # check=True ensures Python raises an error if the script fails
        subprocess.run(["bash", script_path], check=True)
        
        print("[V] Bash script finished successfully.")
        logger.info("Setup script finished successfully.")
        
    except subprocess.CalledProcessError as e:
        print(f"[X] Bash script failed with error: {e}")
        logger.error(f"Script execution failed: {e}")
    except Exception as e:
        print(f"[X] General error: {e}")
        logger.error(f"Error running script: {e}")

# --- Main Entry Point ---
if __name__ == "__main__":
    logger.info("System started")
    
    # Step 1: Get User Input
    collected_data = get_user_input()
    
    if collected_data:
        # Step 2: Save to JSON
        save_to_file(collected_data)
        
        # Step 3: Run the Bash Script (Automation)
        run_setup_script()
    else:
        print("No machines created. Exiting.")