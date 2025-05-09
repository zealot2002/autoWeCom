#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
autoWeCom - Main application entry point
"""

import os
import sys
import wx
from config.settings import APP_NAME, APP_VERSION, WINDOW_WIDTH, WINDOW_HEIGHT, PLATFORM
from module.main_frame import MainFrame

def setup_platform():
    """Setup platform-specific configurations"""
    if PLATFORM == "mac":
        # macOS specific setup
        # Ensure scripts have executable permissions
        rpa_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rpa")
        scripts_dir = os.path.join(rpa_dir, "scripts", "wechat")
        shell_script = os.path.join(rpa_dir, "send_wechat_message.sh")
        
        if os.path.exists(shell_script):
            try:
                os.chmod(shell_script, 0o755)  # Make executable
            except:
                print("Warning: Could not set executable permissions on shell script")
        
        if os.path.exists(scripts_dir):
            for script in os.listdir(scripts_dir):
                if script.endswith(".applescript"):
                    try:
                        os.chmod(os.path.join(scripts_dir, script), 0o755)
                    except:
                        print(f"Warning: Could not set executable permissions on {script}")
    
    elif PLATFORM == "windows":
        # Windows specific setup
        # Nothing specific needed yet
        pass

def main():
    """Main application entry point"""
    # Setup platform-specific configurations
    setup_platform()
    
    app = wx.App(False)
    frame = MainFrame(None, f"{APP_NAME} {APP_VERSION} ({PLATFORM.capitalize()})")
    app.MainLoop()

if __name__ == "__main__":
    main() 