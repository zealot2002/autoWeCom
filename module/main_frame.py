#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main application frame for autoWeCom
"""

import wx
from config.settings import (
    WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT,
    MENU_WIDTH, TOOLBAR_HEIGHT, PRIMARY_COLOR, BACKGROUND_COLOR
)
from module.menu_panel import MenuPanel
from module.content_panel import ContentPanel

class MainFrame(wx.Frame):
    """Main application frame class"""
    
    def __init__(self, parent, title):
        """Initialize the main frame"""
        super(MainFrame, self).__init__(
            parent,
            title=title,
            size=(WINDOW_WIDTH, WINDOW_HEIGHT),
            style=wx.DEFAULT_FRAME_STYLE
        )
        
        # Set minimum size
        self.SetMinSize((WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT))
        
        # Set icon (to be implemented)
        # self.SetIcon(wx.Icon("assets/icon.ico"))
        
        # Initialize UI
        self._init_ui()
        
        # Center the frame
        self.Centre()
        
        # Show the frame
        self.Show(True)
    
    def _init_ui(self):
        """Initialize UI components"""
        # Create main panel
        self.main_panel = wx.Panel(self)
        self.main_panel.SetBackgroundColour(BACKGROUND_COLOR)
        
        # Create status bar
        self.CreateStatusBar()
        self.SetStatusText("Ready")
        
        # Create toolbar
        self._create_toolbar()
        
        # Create main sizer
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create content sizer
        content_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Create menu panel
        self.menu_panel = MenuPanel(self.main_panel, size=(MENU_WIDTH, -1))
        content_sizer.Add(self.menu_panel, 0, wx.EXPAND)
        
        # Create content panel
        self.content_panel = ContentPanel(self.main_panel)
        content_sizer.Add(self.content_panel, 1, wx.EXPAND)
        
        # Add content sizer to main sizer
        main_sizer.Add(content_sizer, 1, wx.EXPAND)
        
        # Set sizer
        self.main_panel.SetSizer(main_sizer)
        
        # Bind events
        self.menu_panel.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_menu_selected)
    
    def _create_toolbar(self):
        """Create the application toolbar"""
        toolbar = self.CreateToolBar()
        toolbar.SetBackgroundColour(PRIMARY_COLOR)
        
        # Add toolbar buttons
        # These will be implemented later with actual icons
        tool1 = toolbar.AddTool(
            wx.ID_ANY, 
            "Settings",
            wx.ArtProvider.GetBitmap(wx.ART_INFORMATION),
            "Application Settings"
        )
        tool2 = toolbar.AddTool(
            wx.ID_ANY, 
            "Help",
            wx.ArtProvider.GetBitmap(wx.ART_HELP),
            "Help"
        )
        
        # Realize the toolbar
        toolbar.Realize()
        
        # Bind events
        self.Bind(wx.EVT_TOOL, self._on_settings, tool1)
        self.Bind(wx.EVT_TOOL, self._on_help, tool2)
    
    def _on_menu_selected(self, event):
        """Handle menu item selection"""
        item_id = event.GetItem().GetId()
        self.content_panel.show_page(item_id)
    
    def _on_settings(self, event):
        """Handle settings button click"""
        wx.MessageBox("Settings dialog will open here", "Settings", wx.OK | wx.ICON_INFORMATION)
    
    def _on_help(self, event):
        """Handle help button click"""
        wx.MessageBox("Help dialog will open here", "Help", wx.OK | wx.ICON_INFORMATION) 