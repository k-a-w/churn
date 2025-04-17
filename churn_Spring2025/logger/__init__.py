import logging #built-in module used for logging
import os #allows us to interact with operating system
from from_root import from_root #returns the root directory of the project
#allows us to build paths relative to the root directory
from datetime import datetime

#creates unique identifier for the log with date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'
log_path = os.path.join(from_root(), log_dir, LOG_FILE)

os.makedirs(log_dir, exist_ok=True)

#Logging Configuration
logging.basicConfig(
    filename = log_path,
    format = "[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level = logging.DEBUG #includes Debug level and above
)