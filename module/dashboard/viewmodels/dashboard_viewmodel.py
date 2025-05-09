#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ViewModel for the Dashboard page
"""

import wx
import logging
from module.dashboard.models.message_model import MessageModel

logger = logging.getLogger("DashboardViewModel")

class DashboardViewModel:
    """ViewModel for the Dashboard page"""
    
    def __init__(self):
        """Initialize the dashboard view model"""
        self.message_model = MessageModel()
        logger.debug("DashboardViewModel initialized")
    
    def set_target(self, target):
        """Set the target contact"""
        self.message_model.target = target
        logger.debug(f"Target set to: {target}")
    
    def set_content(self, content):
        """Set the message content"""
        self.message_model.content = content
        logger.debug(f"Content set, length: {len(content)}")
    
    def send_message(self):
        """Send the message using the model"""
        logger.debug("Sending message via model")
        success, message = self.message_model.send()
        logger.debug(f"Message send result: {success}")
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
    
    def get_message_logs(self):
        """获取消息模型中的日志"""
        return self.message_model.get_logs() 