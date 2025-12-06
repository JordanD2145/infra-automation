# Infra Automation Project 🚀

## 📖 Project Overview
The **Infra Automation Project** is a comprehensive Python-based CLI tool designed to automate system maintenance and monitoring tasks.
The primary goal of this project is to provide a robust infrastructure for tracking system health (CPU, Memory, Disk), managing automated tasks, and handling structured logging.

This project was developed as the final assignment for the Python course, demonstrating modular architecture, object-oriented programming, and configuration management.

## 👤 Submitter Details
* **Student Name:** Jordan Davidov
* **ID:** 313591026
* **Course Name:** Python

## ✨ Key Features
The system includes the following core capabilities:
* **System Resource Monitoring:** Real-time tracking of system performance (CPU usage, Memory load, Disk space).
* **Automated Logging:** A robust logging mechanism that records all system events and errors into the `logs/` directory for auditing.
* **Configuration Management:** Uses external JSON/YAML files located in `configs/` to dynamically control system thresholds without modifying code.
* **Modular Design:** The project is structured as a package (`src/`), ensuring code reusability and clean separation of logic.
* **Error Handling:** Implements comprehensive exception handling to ensure continuous operation.

## 📂 Project Structure
* `src/` - **Source Code**: Contains the main application logic and modules.
* `configs/` - **Configuration**: Stores settings files for easy customization.
* `scripts/` - **Automation Scripts**: Helper scripts for setup and maintenance.
* `logs/` - **Logs**: Destination for all generated log files.
* `requirements.txt` - **Dependencies**: Lists all external Python libraries required.

## ⚙️ Prerequisites
* Python 3.8+
* Git

## 🚀 How to Run
1. **Clone the repository:**
   ```bash
   git clone https://github.com/JordanD2145/infra-automation.git
