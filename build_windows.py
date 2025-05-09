#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Build script for Windows version of autoWeCom
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

# Set platform to windows before importing settings
os.environ["PLATFORM"] = "windows"

# Update config settings file
settings_path = Path(__file__).parent / "config" / "settings.py"
with open(settings_path, "r", encoding="utf-8") as f:
    content = f.read()

if 'PLATFORM = "mac"' in content:
    content = content.replace('PLATFORM = "mac"', 'PLATFORM = "windows"')
    with open(settings_path, "w", encoding="utf-8") as f:
        f.write(content)

# Create requirements_windows.txt if it doesn't exist
if not os.path.exists("requirements_windows.txt"):
    with open("requirements_windows.txt", "w", encoding="utf-8") as f:
        f.write("wxPython>=4.2.0\n")
        f.write("robotframework>=7.0.0\n")
        f.write("robotframework-appiumlibrary\n")
        f.write("pyautogui\n")
        f.write("setuptools>=42.0.0\n")
        f.write("wheel>=0.37.0\n")
        f.write("pypiwin32\n")  # Windows specific dependency

# Install required packages
print("Installing dependencies for Windows build...")
subprocess.call([sys.executable, "-m", "pip", "install", "-r", "requirements_windows.txt"])

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

# Create a Windows icon if needed
windows_icon = ""
if os.path.exists("assets/icon.ico"):
    windows_icon = "--icon=assets/icon.ico"
else:
    windows_icon = None  # 避免传递空字符串

# 修复的 PyInstaller 命令，使用字符串形式
pyinstaller_cmd = [
    sys.executable,
    "-m", "PyInstaller",
    "--name=autoWeCom",
    "--onefile",
    "--windowed"
]

# 添加可选的图标参数
if windows_icon:
    pyinstaller_cmd.append(windows_icon)

# 添加数据文件参数
pyinstaller_cmd.extend([
    "--add-data=config;config",
    "--add-data=rpa/windows;rpa/windows",
    "--add-data=assets;assets"
])

# 添加主脚本
pyinstaller_cmd.append("main.py")

# 执行命令
print("Building Windows application...")
print(f"Running command: {' '.join(pyinstaller_cmd)}")
subprocess.call(pyinstaller_cmd)

print("Build completed! Application is available in the dist directory.")
print("Windows executable created: dist/autoWeCom.exe") 