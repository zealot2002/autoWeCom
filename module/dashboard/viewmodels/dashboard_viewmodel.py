#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ViewModel for the Dashboard page
"""

import wx
from module.dashboard.models.message_model import MessageModel

class DashboardViewModel:
    """ViewModel for the Dashboard page"""
    
    def __init__(self):
        """Initialize the dashboard view model"""
        self.message_model = MessageModel()
    
    def set_target(self, target):
        """Set the target contact"""
        self.message_model.target = target
    
    def set_content(self, content):
        """Set the message content"""
        self.message_model.content = content
    
    def send_message(self):
        """Send the message using the model"""
        success, message = self.message_model.send()
        if success:
            # Update UI or show success message
            return True, message
        else:
            # Show error message
            return False, message
    
    def get_target(self):
        """Get the current target contact"""
        return self.message_model.target
    
    def get_content(self):
        """Get the current message content"""
        return self.message_model.content 