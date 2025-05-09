# autoWeCom

Automated WeChat Work Interaction Application

## Description

autoWeCom is a desktop application built with wxPython that automates WeChat interactions. It uses RPA (Robotic Process Automation) techniques to send messages and perform tasks without requiring the official WeChat API.

## Key Features

- **Message Sending**: Send WeChat messages to contacts directly from the GUI
- **Task Automation**: Set up automated tasks for WeChat interactions
- **MVVM Architecture**: Clean separation of concerns with Model-View-ViewModel pattern
- **Modular Design**: Easily extendable with new functionality modules

## Technical Overview

- **Frontend**: wxPython (Phoenix implementation)
- **Automation**: Robot Framework for RPA functionality
- **Architecture**: MVVM pattern with clear separation of UI, business logic, and data
- **Platform**: macOS compatible (with AppleScript automation)

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/autoWeCom.git
cd autoWeCom

# Install dependencies
pip install -r requirements.txt

# Make sure the RPA scripts are executable
chmod +x rpa/send_wechat_message.sh
chmod +x rpa/scripts/wechat/*.applescript

# Run the application
python main.py
```

## Project Structure

```
autoWeCom/
├── assets/                 # Static resources
├── config/                 # Configuration files
├── core/                   # Core business logic
├── module/                 # UI modules with MVVM structure
│   ├── dashboard/          # Dashboard module for messaging
│   │   ├── models/         # Data models
│   │   ├── viewmodels/     # View models for business logic
│   │   └── views/          # UI components
│   └── automation/         # Automation module for tasks
│       ├── models/         # Data models
│       ├── viewmodels/     # View models for business logic
│       └── views/          # UI components
├── rpa/                    # RPA scripts for WeChat automation
│   ├── scripts/            # AppleScript and shell scripts
│   └── send_wechat_message.sh  # Main message sending script
├── scripts/                # Utility scripts
├── tests/                  # Test suite
├── utils/                  # Utility functions
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
└── setup.py                # Packaging configuration
```

## Dependencies

- wxPython >= 4.2.0
- Robot Framework >= 7.0.0 
- robotframework-appiumlibrary
- pyautogui
- setuptools >= 42.0.0
- wheel >= 0.37.0

## Usage

1. Launch the application with `python main.py`
2. Use the navigation menu on the left to access different modules
3. In the Dashboard, enter the contact name and message content
4. Click "Send" to send the message via WeChat
5. The Automation module allows setting up automated tasks

## Building Executable

To build a standalone executable:

```bash
# Using PyInstaller
pip install pyinstaller
pyinstaller --onefile --windowed --add-data "rpa:rpa" main.py
```

## Notes

- Ensure WeChat is installed and logged in on your system
- The RPA functionality requires macOS and a proper setup for AppleScript permissions
- For better reliability, install the optional `cliclick` tool: `brew install cliclick`

## License

[MIT License](LICENSE)

## Author

Your Name - your.email@example.com 