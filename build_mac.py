#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Build script for macOS version of autoWeCom
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

# Set platform to mac before importing settings
os.environ["PLATFORM"] = "mac"

# Update config settings file
settings_path = Path(__file__).parent / "config" / "settings.py"
with open(settings_path, "r", encoding="utf-8") as f:
    content = f.read()

if 'PLATFORM = "windows"' in content:
    content = content.replace('PLATFORM = "windows"', 'PLATFORM = "mac"')
    with open(settings_path, "w", encoding="utf-8") as f:
        f.write(content)

# Install required packages
print("Installing dependencies for macOS build...")
subprocess.call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Install PyInstaller if not already installed
try:
    import PyInstaller
except ImportError:
    print("Installing PyInstaller...")
    subprocess.call([sys.executable, "-m", "pip", "install", "pyinstaller"])

# Clean previous build artifacts
print("Cleaning previous build artifacts...")
if os.path.exists("build"):
    shutil.rmtree("build")
if os.path.exists("dist"):
    shutil.rmtree("dist")

# 使用更可靠的命令构建方式
pyinstaller_cmd = [
    sys.executable, 
    "-m", "PyInstaller",
    "--name=autoWeCom",
    "--onefile",
    "--windowed",
    "--add-data=config:config",
    "--add-data=rpa/scripts:rpa/scripts",
    "--add-data=rpa/send_wechat_message.sh:rpa/",
    "--add-data=assets:assets",
    "main.py"
]

# 执行命令
print("Building macOS application...")
print(f"Running command: {' '.join(pyinstaller_cmd)}")
subprocess.call(pyinstaller_cmd)

print("Build completed! Application is available in the dist directory.")
print("macOS app created: dist/autoWeCom") 