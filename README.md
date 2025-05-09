# autoWeCom

Automated WeChat Work Interaction Application

## Description

autoWeCom is a desktop application that provides automation tools for WeChat Work (Enterprise WeChat) interactions. It features a modular architecture with a user-friendly interface. The application now supports both macOS and Windows platforms.

## Features

- Dashboard for monitoring activities
- Automation tools for WeChat Work
- Contact management
- Message handling
- Reporting and analytics
- Configuration settings
- **Cross-platform support** for macOS and Windows

## Installation

```bash
# Clone the repository
git clone https://your-repository-url/autoWeCom.git
cd autoWeCom

# For macOS
pip install -r requirements.txt
python main.py

# For Windows
pip install -r requirements_windows.txt
python main.py
```

## Building Executable

### For macOS

```bash
# Build for macOS
python build_mac.py
```

### For Windows

```bash
# Build for Windows
python build_windows.py
```

## Platform-Specific Information

### macOS

The macOS version uses AppleScript for WeChat Work automation. It has been tested on macOS Ventura and above.

### Windows

The Windows version uses PyAutoGUI for automation. It has been tested on Windows 10 and 11 with Enterprise WeChat installed in the default location.

## Project Structure

```
autoWeCom/
├── assets/           # Static resources
├── config/           # Configuration files
├── core/             # Core business logic
├── scripts/          # Utility scripts
├── tests/            # Test suite
├── utils/            # Utility functions
├── views/            # UI components
├── rpa/
│   ├── scripts/      # macOS automation scripts
│   ├── windows/      # Windows automation scripts
├── main.py           # Entry point
├── build_mac.py      # macOS build script
├── build_windows.py  # Windows build script
└── setup.py          # Packaging configuration
```

## Configuration

The platform can be manually configured in `config/settings.py`:

```python
# Change this to 'windows' to build for Windows
PLATFORM = "mac"  # Options: 'mac', 'windows'
```

## License

[MIT License](LICENSE)

## Author

Your Name - your.email@example.com 