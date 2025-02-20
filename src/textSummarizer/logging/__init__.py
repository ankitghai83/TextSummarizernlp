## This custom looging file can be used in any projects to log the information
import os
import sys
import logging

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir="logs"
log_filepath=os.path.join(log_dir,"logfile.log")
os.makedirs(log_dir,exist_ok=True)
# logging.FileHandler : This is used to write the logs to the file
# logging.StreamHandler : This is used to write the logs to the console
logging.basicConfig(level=logging.INFO,format=logging_str,handlers=[logging.FileHandler(log_filepath),logging.StreamHandler(sys.stdout)])

logger=logging.getLogger("textSummarizerLogger")