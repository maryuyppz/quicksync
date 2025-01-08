import os
import shutil
from datetime import datetime
import filecmp
import logging

logging.basicConfig(level=logging.INFO)

class QuickSync:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def sync(self):
        logging.info("Starting synchronization process.")
        if not os.path.exists(self.source):
            logging.error(f"Source path '{self.source}' does not exist.")
            return

        if not os.path.exists(self.destination):
            logging.info(f"Destination path '{self.destination}' does not exist. Creating...")
            os.makedirs(self.destination)

        self.copy_files(self.source, self.destination)
        logging.info("Synchronization process completed.")

    def copy_files(self, src, dest):
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dest_path = os.path.join(dest, item)

            if os.path.isdir(src_path):
                logging.info(f"Entering directory: {src_path}")
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)
                self.copy_files(src_path, dest_path)
            else:
                if not os.path.exists(dest_path) or not filecmp.cmp(src_path, dest_path, shallow=False):
                    logging.info(f"Copying file '{src_path}' to '{dest_path}'")
                    shutil.copy2(src_path, dest_path)
                else:
                    logging.info(f"File '{src_path}' is already up-to-date.")

if __name__ == "__main__":
    source_directory = "C:\\path\\to\\source"
    destination_directory = "C:\\path\\to\\destination"
    
    sync = QuickSync(source_directory, destination_directory)
    sync.sync()