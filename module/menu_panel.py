#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Menu panel for autoWeCom
"""

import wx
from config.settings import PRIMARY_COLOR, SECONDARY_COLOR, TEXT_COLOR

class MenuPanel(wx.Panel):
    """Left side menu panel"""
    
    def __init__(self, parent, size=(-1, -1)):
        """Initialize the menu panel"""
        super(MenuPanel, self).__init__(parent, size=size)
        
        # Set background color
        self.SetBackgroundColour("#FFFFFF")
        
        # Initialize UI
        self._init_ui()
    
    def _init_ui(self):
        """Initialize UI components"""
        # Create main sizer
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create title
        title = wx.StaticText(self, label="Navigation")
        title.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        title.SetForegroundColour(PRIMARY_COLOR)
        main_sizer.Add(title, 0, wx.ALL | wx.EXPAND, 10)
        
        # Create separator
        line = wx.StaticLine(self, style=wx.LI_HORIZONTAL)
        main_sizer.Add(line, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        
        # Create menu list
        self.menu_list = wx.ListView(
            self,
            style=wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_NO_HEADER
        )
        
        # Configure menu list
        self.menu_list.InsertColumn(0, "Menu")
        self.menu_list.SetBackgroundColour("#FFFFFF")
        
        # Add menu items
        menu_items = [
            ("Dashboard", 0),
            ("Automation", 1),
            ("Contacts", 2),
            ("Messages", 3),
            ("Reports", 4),
            ("Settings", 5)
        ]
        
        for idx, (name, item_id) in enumerate(menu_items):
            self.menu_list.InsertItem(idx, name)
            self.menu_list.SetItemData(idx, item_id)
        
        # Adjust column width
        self.menu_list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        
        # Add menu list to sizer
        main_sizer.Add(self.menu_list, 1, wx.EXPAND | wx.ALL, 10)
        
        # Set sizer
        self.SetSizer(main_sizer)
        
        # Bind events
        self.menu_list.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_item_selected)
        
        # Select first item by default
        self.menu_list.Select(0)
    
    def _on_item_selected(self, event):
        """Handle menu item selection"""
        # Forward the event to the parent
        wx.PostEvent(self.GetParent(), event) 