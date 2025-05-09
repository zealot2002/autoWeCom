#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Content panel for autoWeCom
"""

import wx
from config.settings import BACKGROUND_COLOR

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
        """Create content pages"""
        # Dashboard page
        self.pages[0] = DashboardPage(self)
        self.main_sizer.Add(self.pages[0], 1, wx.EXPAND)
        
        # Automation page
        self.pages[1] = AutomationPage(self)
        self.main_sizer.Add(self.pages[1], 1, wx.EXPAND)
        
        # Contacts page
        self.pages[2] = ContactsPage(self)
        self.main_sizer.Add(self.pages[2], 1, wx.EXPAND)
        
        # Messages page
        self.pages[3] = MessagesPage(self)
        self.main_sizer.Add(self.pages[3], 1, wx.EXPAND)
        
        # Reports page
        self.pages[4] = ReportsPage(self)
        self.main_sizer.Add(self.pages[4], 1, wx.EXPAND)
        
        # Settings page
        self.pages[5] = SettingsPage(self)
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
    """Base class for content pages"""
    
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
        
        # Create content (to be overridden by child classes)
        content = wx.StaticText(self, label="Content to be implemented")
        main_sizer.Add(content, 1, wx.ALL | wx.CENTER, 20)
        
        # Set sizer
        self.SetSizer(main_sizer)


class DashboardPage(BasePage):
    """Dashboard page"""
    
    def __init__(self, parent):
        """Initialize the dashboard page"""
        super(DashboardPage, self).__init__(parent, "Dashboard")


class AutomationPage(BasePage):
    """Automation page"""
    
    def __init__(self, parent):
        """Initialize the automation page"""
        super(AutomationPage, self).__init__(parent, "Automation")


class ContactsPage(BasePage):
    """Contacts page"""
    
    def __init__(self, parent):
        """Initialize the contacts page"""
        super(ContactsPage, self).__init__(parent, "Contacts")


class MessagesPage(BasePage):
    """Messages page"""
    
    def __init__(self, parent):
        """Initialize the messages page"""
        super(MessagesPage, self).__init__(parent, "Messages")


class ReportsPage(BasePage):
    """Reports page"""
    
    def __init__(self, parent):
        """Initialize the reports page"""
        super(ReportsPage, self).__init__(parent, "Reports")


class SettingsPage(BasePage):
    """Settings page"""
    
    def __init__(self, parent):
        """Initialize the settings page"""
        super(SettingsPage, self).__init__(parent, "Settings") 