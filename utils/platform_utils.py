#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Platform-specific utility functions
"""

import os
import sys
import subprocess
from config.settings import PLATFORM

def get_platform():
    """Get the current platform from settings"""
    return PLATFORM

def is_windows():
    """Check if the current platform is Windows"""
    return PLATFORM == "windows"

def is_mac():
    """Check if the current platform is macOS"""
    return PLATFORM == "mac"

def get_app_resource_path(relative_path):
    """Get the correct path to application resources, working both in development and when packaged"""
    if getattr(sys, 'frozen', False):
        # When running as bundled app
        base_path = sys._MEIPASS
    else:
        # When running in development
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    return os.path.join(base_path, relative_path)

def run_platform_script(script_name, *args):
    """Run a platform-specific script with arguments"""
    if is_windows():
        # Windows script execution
        script_path = get_app_resource_path(os.path.join("rpa", "windows", script_name))
        if script_name.endswith(".bat"):
            cmd = ["cmd", "/c", script_path]
        else:
            cmd = [sys.executable, script_path]
        
        cmd.extend(args)
        return subprocess.Popen(cmd)
    
    else:  # macOS
        # macOS script execution
        script_path = get_app_resource_path(os.path.join("rpa", script_name))
        if script_name.endswith(".sh"):
            cmd = ["bash", script_path]
        else:
            cmd = [sys.executable, script_path]
        
        cmd.extend(args)
        return subprocess.Popen(cmd)

def get_wechat_executable_path():
    """Get the path to the WeChat Work executable for the current platform"""
    if is_windows():
        # Default Windows installation path
        return "C:\\Program Files (x86)\\WXWork\\WXWork.exe"
    else:
        # macOS app bundle
        return "/Applications/企业微信.app" 