#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
View for the Dashboard page
"""

import wx
from config.settings import BACKGROUND_COLOR, PRIMARY_COLOR
from views.dashboard.viewmodels.dashboard_viewmodel import DashboardViewModel

class DashboardView(wx.Panel):
    """View class for the Dashboard page"""
    
    def __init__(self, parent):
        """Initialize the dashboard view"""
        super(DashboardView, self).__init__(parent)
        
        # Set page name
        self.SetName("Dashboard")
        
        # Set background color
        self.SetBackgroundColour(BACKGROUND_COLOR)
        
        # Create ViewModel
        self.viewmodel = DashboardViewModel()
        
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
        
        # Create form panel
        form_panel = wx.Panel(self)
        form_panel.SetBackgroundColour(wx.WHITE)
        
        # Create form sizer
        form_sizer = wx.GridBagSizer(10, 10)
        
        # Add target contact input
        target_label = wx.StaticText(form_panel, label="Target Contact:")
        form_sizer.Add(target_label, pos=(0, 0), flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=10)
        
        self.target_input = wx.TextCtrl(form_panel, size=(300, -1))
        form_sizer.Add(self.target_input, pos=(0, 1), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=10)
        
        # Add content input
        content_label = wx.StaticText(form_panel, label="Content:")
        form_sizer.Add(content_label, pos=(1, 0), flag=wx.ALL | wx.ALIGN_TOP, border=10)
        
        self.content_input = wx.TextCtrl(form_panel, style=wx.TE_MULTILINE, size=(300, 100))
        form_sizer.Add(self.content_input, pos=(1, 1), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=10)
        
        # Add send button
        self.send_button = wx.Button(form_panel, label="Send")
        self.send_button.SetBackgroundColour(PRIMARY_COLOR)
        self.send_button.SetForegroundColour(wx.WHITE)
        form_sizer.Add(self.send_button, pos=(2, 2), flag=wx.ALL | wx.ALIGN_RIGHT, border=10)
        
        # Make columns expandable
        form_sizer.AddGrowableCol(1)
        form_sizer.AddGrowableRow(1)
        
        # Set form sizer
        form_panel.SetSizer(form_sizer)
        
        # Add form panel to main sizer
        main_sizer.Add(form_panel, 1, wx.EXPAND | wx.ALL, 20)
        
        # Bind events
        self.send_button.Bind(wx.EVT_BUTTON, self._on_send)
        
        # Set sizer
        self.SetSizer(main_sizer)
    
    def _on_send(self, event):
        """Handle send button click"""
        # Update the ViewModel with the current values
        self.viewmodel.set_target(self.target_input.GetValue())
        self.viewmodel.set_content(self.content_input.GetValue())
        
        # Send the message through the ViewModel
        success, message = self.viewmodel.send_message()
        
        if success:
            wx.MessageBox(message, "Success", wx.OK | wx.ICON_INFORMATION)
            # Update status bar
            frame = self.GetTopLevelParent()
            frame.SetStatusText(message)
        else:
            wx.MessageBox(message, "Error", wx.OK | wx.ICON_ERROR) 