import json
import sys
import os
import subprocess

# Setup path to import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.machine import Machine
from src.logger import logger

def validate_input(os_type, cpu, ram):
    """
    Validates user input according to project rules.
    Returns True if valid, False if invalid.
    """
    # 1. Check OS type
    valid_os = ["Ubuntu", "CentOS", "Linux"]
    if os_type not in valid_os:
        print(f"[!] Error: OS must be one of: {valid_os}")
        return False

    # 2. Check CPU format (must contain 'vCPU')
    if "vCPU" not in cpu:
        print("[!] Error: CPU must contain 'vCPU' (e.g., 2vCPU)")
        return False

    # 3. Check RAM format (must contain 'GB')
    if "GB" not in ram:
        print("[!] Error: RAM must contain 'GB' (e.g., 4GB)")
        return False

    return True

def get_user_input():
    """Collects machine details from the user with validation."""
    machines_list = []
    print("--- Welcome to Infra Automation ---")
    
    while True:
        name = input("Enter machine name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
            
        # Loop until valid input is received
        while True:
            os_type = input("Enter OS (Ubuntu/CentOS): ")
            cpu = input("Enter CPU (e.g., 2vCPU): ")
            ram = input("Enter RAM (e.g., 4GB): ")

            # Call our new validation function (The "Traffic Cop")
            if validate_input(os_type, cpu, ram):
                # If valid, break the inner loop and proceed
                break
            else:
                print(">>> Invalid input. Please try again.\n")
        
        # Create and save the machine
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
    """Executes the Bash script using Python's subprocess module."""
    script_path = os.path.join('scripts', 'setup_nginx.sh')
    
    print(f"\n[INFO] Python is now running the Bash script: {script_path}...")
    logger.info(f"Starting execution of {script_path}")

    try:
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
    
    collected_data = get_user_input()
    
    if collected_data:
        save_to_file(collected_data)
        run_setup_script()
    else:
        print("No machines created. Exiting.")