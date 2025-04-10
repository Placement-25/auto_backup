# 🔐 Automated System Backup Script

A robust and production-ready Python script that **automatically backs up specified directories** into a timestamped `.zip` file. Designed for ease of use, automation, and reliability.

---

## 🚀 Features

- 🔄 Backs up multiple directories recursively
- 📁 Creates timestamped `.zip` archives
- 📜 Logs every backup operation and warning
- 📦 Compresses files to save space
- ✅ Designed for daily/weekly automation (e.g., cron, task scheduler)

---

## 📦 Requirements

- Python 3.7+
- No external libraries required (uses `os`, `zipfile`, `argparse`, `logging`)

---

## ⚙️ Usage

### 📥 1. Install Python dependencies

This script only uses Python's standard library — no additional setup required.

---

### ▶️ 2. Run the script

```bash
python auto_backup.py --source /path/to/folder1 /path/to/folder2 --output ./my_backups --log backup.log
