import logging
import os

def setup_logging():
    """
    Configures the project's logging system.
    Logs will be saved to 'logs/provisioning.log'.
    """
    # Define the directory where logs will be stored
    log_dir = 'logs'
    
    # Check if the directory exists. If not, create it automatically.
    # This prevents errors if the user forgot to create the folder.
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Configure the logging settings
    # 'filename': Specifies the file where logs are saved. Python creates it if missing.
    # 'level': Sets the threshold for tracking (INFO means we track almost everything).
    # 'format': Defines how the log message looks (Time - Level - Message).
    logging.basicConfig(
        filename=os.path.join(log_dir, 'provisioning.log'),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    return logging.getLogger()

# Create a global logger instance to be used across the project
logger = setup_logging()
