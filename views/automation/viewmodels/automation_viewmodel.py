#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ViewModel for the Automation page
"""

from views.automation.models.automation_model import AutomationModel

class AutomationViewModel:
    """ViewModel for the Automation page"""
    
    def __init__(self):
        """Initialize the automation view model"""
        self.model = AutomationModel()
        # Pre-populate with some example tasks
        self.model.add_task({
            "name": "Daily Report",
            "description": "Send daily report to team leads",
            "schedule": "Daily at 17:00",
            "status": "Inactive"
        })
        self.model.add_task({
            "name": "Welcome Message",
            "description": "Send welcome message to new members",
            "schedule": "On trigger",
            "status": "Active"
        })
    
    def get_tasks(self):
        """Get all automation tasks"""
        return self.model.get_tasks()
    
    def add_task(self, task):
        """Add a new automation task"""
        return self.model.add_task(task)
    
    def remove_task(self, task_id):
        """Remove an automation task"""
        return self.model.remove_task(task_id)
    
    def start_task(self, task_id):
        """Start an automation task"""
        result = self.model.start_task(task_id)
        if result and task_id < len(self.model.tasks):
            self.model.tasks[task_id]["status"] = "Active"
        return result
    
    def stop_task(self, task_id):
        """Stop an automation task"""
        result = self.model.stop_task(task_id)
        if result and task_id < len(self.model.tasks):
            self.model.tasks[task_id]["status"] = "Inactive"
        return result 