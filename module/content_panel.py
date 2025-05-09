#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Content panel for autoWeCom
"""

import wx
from config.settings import BACKGROUND_COLOR, PRIMARY_COLOR

# Import views from MVVM structure
from module.dashboard.views.dashboard_view import DashboardView
from module.automation.views.automation_view import AutomationView

class ContentPanel(wx.Panel):
    """Right side content panel"""
    
    def __init__(self, parent):
        """Initialize the content panel"""
        super(ContentPanel, self).__init__(parent)
        
        # Set background color
        self.SetBackgroundColour(BACKGROUND_COLOR)
        
        # Create pages dictionary
        self.pages = {}
        
        # Initialize UI
        self._init_ui()
        
        # Create pages
        self._create_pages()
        
        # Show default page
        self.show_page(0)
    
    def _init_ui(self):
        """Initialize UI components"""
        # Create main sizer
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Set sizer
        self.SetSizer(self.main_sizer)
    
    def _create_pages(self):
        """Create content pages using MVVM structure"""
        # Dashboard page
        self.pages[0] = DashboardView(self)
        self.main_sizer.Add(self.pages[0], 1, wx.EXPAND)
        
        # Automation page
        self.pages[1] = AutomationView(self)
        self.main_sizer.Add(self.pages[1], 1, wx.EXPAND)
        
        # Contacts page (using base page until implemented with MVVM)
        self.pages[2] = BasePage(self, "Contacts")
        self.main_sizer.Add(self.pages[2], 1, wx.EXPAND)
        
        # Messages page (using base page until implemented with MVVM)
        self.pages[3] = BasePage(self, "Messages")
        self.main_sizer.Add(self.pages[3], 1, wx.EXPAND)
        
        # Reports page (using base page until implemented with MVVM)
        self.pages[4] = BasePage(self, "Reports")
        self.main_sizer.Add(self.pages[4], 1, wx.EXPAND)
        
        # Settings page (using base page until implemented with MVVM)
        self.pages[5] = BasePage(self, "Settings")
        self.main_sizer.Add(self.pages[5], 1, wx.EXPAND)
        
        # Hide all pages initially
        for page in self.pages.values():
            page.Hide()
    
    def show_page(self, page_id):
        """Show the specified page and hide others"""
        # Hide all pages
        for page in self.pages.values():
            page.Hide()
        
        # Show the selected page
        if page_id in self.pages:
            self.pages[page_id].Show()
            
            # Update status bar
            frame = self.GetTopLevelParent()
            page_name = self.pages[page_id].GetName()
            frame.SetStatusText(f"Current page: {page_name}")
        
        # Refresh layout
        self.Layout()


class BasePage(wx.Panel):
    """Base class for content pages (temporary until all MVVM pages are implemented)"""
    
    def __init__(self, parent, name="Base Page"):
        """Initialize the base page"""
        super(BasePage, self).__init__(parent)
        
        # Set page name
        self.SetName(name)
        
        # Set background color
        self.SetBackgroundColour(BACKGROUND_COLOR)
        
        # Initialize UI
        self._init_ui()
    
    def _init_ui(self):
        """Initialize UI components"""
        # Create main sizer
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create title
        title = wx.StaticText(self, label=self.GetName())
        title.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        main_sizer.Add(title, 0, wx.ALL | wx.CENTER, 20)
        
        # Create content (placeholder)
        content = wx.StaticText(self, label="This page will be implemented with MVVM pattern soon")
        content.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        main_sizer.Add(content, 1, wx.ALL | wx.CENTER, 20)
        
        # Set sizer
        self.SetSizer(main_sizer) 