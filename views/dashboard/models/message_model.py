#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Message model for the Dashboard page
"""

class MessageModel:
    """Model class for message data"""
    
    def __init__(self, target="", content=""):
        """Initialize the message model"""
        self.target = target
        self.content = content
    
    def validate(self):
        """Validate the message data"""
        if not self.target:
            return False, "Target contact cannot be empty"
        
        if not self.content:
            return False, "Message content cannot be empty"
        
        return True, "Valid message data"
    
    def send(self):
        """Send the message (placeholder)"""
        # This would be implemented to actually send the message
        # through the appropriate channel
        valid, message = self.validate()
        if not valid:
            return False, message
        
        # Placeholder for actual sending logic
        return True, f"Message to '{self.target}' sent successfully" 