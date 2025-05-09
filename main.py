#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
autoWeCom - Main application entry point
"""

import wx
from config.settings import APP_NAME, APP_VERSION, WINDOW_WIDTH, WINDOW_HEIGHT
from views.main_frame import MainFrame

def main():
    """Main application entry point"""
    app = wx.App(False)
    frame = MainFrame(None, f"{APP_NAME} {APP_VERSION}")
    app.MainLoop()

if __name__ == "__main__":
    main() 