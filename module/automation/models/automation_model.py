#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Model for the Automation page
"""

class AutomationModel:
    """Model class for automation data"""
    
    def __init__(self):
        """Initialize the automation model"""
        self.tasks = []
        self.active_tasks = []
    
    def add_task(self, task):
        """Add a new automation task"""
        self.tasks.append(task)
        return True
    
    def remove_task(self, task_id):
        """Remove an automation task"""
        if task_id < len(self.tasks):
            del self.tasks[task_id]
            return True
        return False
    
    def get_tasks(self):
        """Get all tasks"""
        return self.tasks
    
    def start_task(self, task_id):
        """Start an automation task"""
        if task_id < len(self.tasks):
            task = self.tasks[task_id]
            if task not in self.active_tasks:
                self.active_tasks.append(task)
            return True
        return False
    
    def stop_task(self, task_id):
        """Stop an automation task"""
        if task_id < len(self.tasks):
            task = self.tasks[task_id]
            if task in self.active_tasks:
                self.active_tasks.remove(task)
            return True
        return False 