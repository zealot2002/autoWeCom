# Platform Configuration Guide

This guide explains how to configure and build autoWeCom for different platforms.

## Configuring the Platform

autoWeCom supports both macOS and Windows. The platform is configured in the `config/settings.py` file.

### Setting Platform Manually

Open the `config/settings.py` file and look for the platform configuration:

```python
# Platform settings
# Change this to 'windows' to build for Windows
PLATFORM = "mac"  # Options: 'mac', 'windows'
```

Change the value to either `"mac"` or `"windows"` depending on your target platform.

## Building for Different Platforms

### Building for macOS

1. Ensure the platform is set to `"mac"` in `config/settings.py`
2. Run the macOS build script:

```bash
python build_mac.py
```

3. The macOS application will be created in the `dist` directory

### Building for Windows

1. Ensure the platform is set to `"windows"` in `config/settings.py`
2. Run the Windows build script:

```bash
python build_windows.py
```

3. The Windows executable will be created in the `dist` directory

## Switching Between Platforms During Development

When developing and testing for both platforms, you can use the build scripts to automatically switch the platform setting:

- `build_mac.py` will automatically change the platform to `"mac"`
- `build_windows.py` will automatically change the platform to `"windows"`

## Platform-Specific Dependencies

- macOS dependencies are listed in `requirements.txt`
- Windows dependencies are listed in `requirements_windows.txt`

When developing, you should install the dependencies for your development platform:

```bash
# On macOS
pip install -r requirements.txt

# On Windows
pip install -r requirements_windows.txt
```

## Troubleshooting

### macOS Specific Issues

- If scripts aren't executing, check their permissions. The application should automatically make scripts executable during startup.
- AppleScript automation might need adjustments based on your macOS version.

### Windows Specific Issues

- Screen coordinates in the PyAutoGUI automation might need adjustment based on your screen resolution and Windows scaling settings.
- The Enterprise WeChat application might be installed in a different location. Check the path in `utils/platform_utils.py` if needed. 