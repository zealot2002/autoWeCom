"""
Application settings for autoWeCom
"""

APP_NAME = "autoWeCom"
APP_VERSION = "0.1.0"
APP_DESCRIPTION = "Automated WeChat Work Interaction Application"

# Platform settings
# Change this to 'windows' to build for Windows
PLATFORM = "windows"  # Options: 'mac', 'windows'

# Window settings
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
WINDOW_MIN_WIDTH = 800
WINDOW_MIN_HEIGHT = 600

# UI settings
MENU_WIDTH = 200
TOOLBAR_HEIGHT = 50

# Theme settings
PRIMARY_COLOR = "#2196F3"  # Blue
SECONDARY_COLOR = "#FF9800"  # Orange
BACKGROUND_COLOR = "#F5F5F5"  # Light gray
TEXT_COLOR = "#333333"  # Dark gray

# Platform-specific paths
if PLATFORM == "mac":
    RPA_SCRIPTS_DIR = "rpa/scripts/wechat"
elif PLATFORM == "windows":
    RPA_SCRIPTS_DIR = "rpa/windows/scripts"
else:
    raise ValueError(f"Unsupported platform: {PLATFORM}. Use 'mac' or 'windows'") 