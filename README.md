# Input-monitoring-tool
Input Monitoring Tool
Project Description:
The Input Monitoring Tool is a Python-based application that monitors and logs keyboard and mouse inputs in real-time. It captures keystrokes and mouse movements, storing them for analysis or auditing purposes. This tool can be useful for monitoring user activity, debugging applications, or understanding user behavior.

Features:
Keyboard Input Monitoring: Captures keystrokes including key presses and releases.
Mouse Input Monitoring: Tracks mouse movements, clicks, and scroll events.
Real-time Logging: Logs inputs with timestamps for detailed analysis.
Cross-platform: Works on Windows, macOS, and Linux systems.
Configurable Settings: Adjust logging frequency and output format.
Getting Started:
Clone the Repository:

Clone this repository to your local machine.
Install Dependencies:

Ensure you have Python 3.x installed.
Install required libraries using pip:
pip install pynput
Run the Program:

Open a terminal or command prompt.
Navigate to the project directory.
Run the main script:
python input_monitor.py
Usage:

The tool starts monitoring keyboard and mouse inputs immediately.
Press Esc key to stop the monitoring and exit the program.
Output:

Input logs are saved in the input_logs.txt file in the project directory.
Each log entry includes timestamp, event type (keyboard/mouse), and details (key code, mouse position, etc.).
Notes:
Ensure the tool is used responsibly and complies with local laws regarding monitoring and privacy.
Customize the logging behavior by modifying the script according to specific requirements.
