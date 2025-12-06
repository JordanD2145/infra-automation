# Import the logger we created in the previous step to record events
from src.logger import logger

class Machine:
    def __init__(self, name, os_type, cpu, ram):
        """
        Initialize a new Machine instance.
        This function runs automatically when a new machine is created.
        """
        self.name = name       # Store the machine name
        self.os_type = os_type # Store the operating system type
        self.cpu = cpu         # Store the CPU specifications
        self.ram = ram         # Store the RAM size
        
        # Log the creation of the new machine instance
        logger.info(f"Machine created: {self.name}, OS: {self.os_type}")

    def to_dict(self):
        """
        Convert the machine object to a dictionary (key-value pairs).
        Useful for saving data to JSON files later.
        """
        return {
            "name": self.name,
            "os": self.os_type,
            "cpu": self.cpu,
            "ram": self.ram
        }