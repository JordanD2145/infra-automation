# DevOps Infrastructure Provisioning Project 🚀

A modular automation tool designed to simulate infrastructure provisioning and service configuration.
This project was developed as part of a DevOps course to demonstrate Python and Bash integration.

## 📋 Project Overview
The tool allows users to:
1. Define Virtual Machines (VMs) dynamically via CLI.
2. Save configurations to a JSON file.
3. Automatically execute a Bash script to simulate Nginx installation using Python's `subprocess`.
4. Log all activities to a dedicated log file.

## 📂 Project Structure
* `src/` - Core Python logic (Main script, Machine class, Logger).
* `scripts/` - Bash scripts for automation (e.g., `setup_nginx.sh`).
* `configs/` - Stores the generated `instances.json`.
* `logs/` - Stores system logs (`provisioning.log`).

## ⚙️ Prerequisites
* Python 3.x
* Git
* Linux/Mac environment (or Git Bash on Windows)

## 🚀 How to Run
1. **Clone the repository:**
   ```bash
   git clone <https://github.com/JordanD2145/infra-automation.git
   
   >
   cd infra-automation
# run the project -in terminal - python src/main.py

   # Just to make it clear , i was trubling in installing nginx in windows OS so got help and made it by echo like it is a real installtion
