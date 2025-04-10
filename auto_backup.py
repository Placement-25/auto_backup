import os
import zipfile
import logging
from datetime import datetime
import argparse
from pathlib import Path

class BackupManager:
    def __init__(self, source_dirs, backup_dir="backups", log_file="backup.log"):
        self.source_dirs = [Path(d).resolve() for d in source_dirs]
        self.backup_dir = Path(backup_dir).resolve()
        self.log_file = log_file
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.setup_logger()
        self.ensure_backup_dir()

    def setup_logger(self):
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        logging.info("Backup process initialized.")

    def ensure_backup_dir(self):
        if not self.backup_dir.exists():
            self.backup_dir.mkdir(parents=True)
            logging.info(f"Created backup directory: {self.backup_dir}")

    def create_backup(self):
        backup_file = self.backup_dir / f"backup_{self.timestamp}.zip"
        with zipfile.ZipFile(backup_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for src_dir in self.source_dirs:
                if not src_dir.exists():
                    logging.warning(f"Source directory not found: {src_dir}")
                    continue
                for root, _, files in os.walk(src_dir):
                    for file in files:
                        file_path = Path(root) / file
                        arcname = file_path.relative_to(src_dir.parent)
                        zipf.write(file_path, arcname)
                        logging.debug(f"Added {file_path} as {arcname}")
        logging.info(f"Backup created successfully: {backup_file}")
        print(f"Backup complete: {backup_file}")

    def run(self):
        try:
            self.create_backup()
        except Exception as e:
            logging.error(f"Backup failed: {str(e)}")
            print(f"Error during backup: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated System Backup Script")
    parser.add_argument(
        "--source", "-s", nargs='+', required=True, help="List of source directories to backup"
    )
    parser.add_argument(
        "--output", "-o", default="backups", help="Output directory for backup ZIP"
    )
    parser.add_argument(
        "--log", "-l", default="backup.log", help="Log file name"
    )

    args = parser.parse_args()
    manager = BackupManager(args.source, args.output, args.log)
    manager.run()
